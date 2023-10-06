#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <libgen.h>
#include <ctype.h>
#include <getopt.h>

#define PACKED __attribute__((__packed__))

#define ERROR_INCORRECT_ARG_NUMBER 1
#define ERROR_AMSDOS_HEADER_PRESENT 2

#define FILE_TYPE_BASIC 0
#define FILE_TYPE_BINARY 2

typedef struct PACKED {
    uint8_t user_number;
    char name[8];
    char extension[3];
    uint8_t filename_padding[4];
} filename;

typedef struct PACKED {
    filename file;
    uint8_t block_number;
    uint8_t last_block;
    uint8_t file_type;
    uint16_t data_length;
    uint16_t data_location;
    uint8_t first_block;
    uint16_t logical_length;
    uint16_t entry_address;
    uint8_t media_header_padding[36];
} media_header;

typedef struct PACKED {
    media_header fields;
    uint8_t file_length[3];
    uint16_t checksum;
    uint8_t amsdos_header_padding[59];
} amsdos_header;

typedef struct {
    char *filepath;
    char *filename;
    long size;
    amsdos_header header;
    uint8_t *content;
} amsdos_file;

amsdos_file *load_file(char *file_path) {
    FILE *file;
    amsdos_file *content;

    content = malloc(sizeof(amsdos_file));

    content->filepath = strdup(file_path);
    content->filename = strdup(basename(file_path));

    file = fopen(file_path, "rb");
    fseek(file, 0, SEEK_END);
    content->size = ftell(file);
    fseek(file, 0, SEEK_SET);

    content->content = malloc(content->size);
    fread(content->content, content->size, 1, file);
    fclose(file);

    return content;
}

uint8_t string2filetype(const char *string) {
    if (string[0] != 'b' && string[0] != 'B') return FILE_TYPE_BINARY;
    if (string[1] == 'a' || string[1] == 'A') return FILE_TYPE_BASIC;
    return FILE_TYPE_BINARY;
}

uint16_t string2word(const char *string) {
    unsigned int word = 0;
    sscanf(string, "%4x", &word);
    return (uint16_t)word;
}

uint16_t compute_checksum(const amsdos_header *header) {
    uint8_t *raw = NULL;
    uint16_t checksum = 0;
    int i;

    raw = (uint8_t *)header;

    for (i = 0; i < 67; i++) checksum += raw[i];

    return checksum;
}

bool has_amsdos_header(const amsdos_file *file) {
    amsdos_header *header;
    uint16_t checksum;

    if (file->size <= sizeof(amsdos_header)) return false;

    header = (amsdos_header *)(file->content);
    checksum = compute_checksum(header);

    return checksum == header->checksum;
}

void print_usage() {
    printf("\nUsage: addamsdosheader [options] <filename>\n");
    printf("Options:\n");
    printf("  -t, --type <type>     File type: basic or binary\n");
    printf("  -s, --start <start>   Hexadecimal address at which the file will be loaded\n");
    printf("  -e, --entry <entry>   Hexadecimal address of the entry point (binary)\n");
    printf("  -h, --help            Display this help message\n");
}

void copy_string_toupper(const char *src, char *dst, int maxlen) {
    int i;

    for (i = 0; src[i] != '\0' && src[i] != '.' && i < maxlen; i++) {
        dst[i] = toupper(src[i]);
    }
}

void init_header(amsdos_file *file, uint8_t type, uint16_t start, uint16_t entry) {
    char *extension;

    memset((void *)(&file->header), 0, sizeof(amsdos_header));

    /* Initialize file name and extension */
    memset((void *)(&file->header.fields.file.name), 0x20, 8);
    memset((void *)(&file->header.fields.file.extension), 0x20, 3);

    copy_string_toupper(file->filename, file->header.fields.file.name, 8);

    extension = strchr(file->filename, '.');
    if (extension != NULL) {
        copy_string_toupper(extension + 1, file->header.fields.file.extension, 3);
    }

    /* Initialize file type and memory */
    file->header.fields.file_type = type;
    file->header.fields.data_location = start;
    file->header.fields.logical_length = file->size;
    file->header.fields.entry_address = entry;

    /* Initialize file size */
    file->header.file_length[0] = file->size & 0xFF;
    file->header.file_length[1] = (file->size >> 8) & 0xFF;
    file->header.file_length[2] = (file->size >> 16) & 0xFF;

    /* Compute checksum */
    file->header.checksum = compute_checksum(&file->header);
}

void write_file(const amsdos_file *amsfile) {
    FILE *file;

    file = fopen(amsfile->filepath, "wb");
    fwrite(&amsfile->header, 1, sizeof(amsdos_header), file);
    fwrite(amsfile->content, amsfile->size, 1, file);
    fclose(file);
}

int main(int argc, char **argv) {
    int opt;
    char *file_path = NULL;
    uint8_t file_type = FILE_TYPE_BINARY;
    uint16_t start = 0;
    uint16_t entry = 0;

    while ((opt = getopt(argc, argv, "t:s:e:h")) != -1) {
        switch (opt) {
            case 't':
                if (strcasecmp(optarg, "basic") == 0) {
                    file_type = FILE_TYPE_BASIC;
                } else if (strcasecmp(optarg, "binary") != 0) {
                    fprintf(stderr, "Invalid file type: %s\n", optarg);
                    return 1;
                }
                break;
            case 's':
                start = string2word(optarg);
                break;
            case 'e':
                entry = string2word(optarg);
                break;
            case 'h':
                print_usage();
                return 0;
            default:
                fprintf(stderr, "Usage: %s [-t type] [-s start] [-e entry] [-h] <filename>\n", argv[0]);
                return 1;
        }
    }

    if (optind != argc - 1) {
        fprintf(stderr, "Error: Please provide a filename.\n");
        print_usage();
        return 1;
    } else {
        file_path = argv[optind];
    }

    amsdos_file *file = load_file(file_path);

    if (has_amsdos_header(file)) {
        printf("\nFile '%s' already has AMSDOS header\n", file_path);
        return ERROR_AMSDOS_HEADER_PRESENT;
    }

    init_header(file, file_type, start, entry);

    write_file(file);

    printf("\nAMSDOS header added to '%s'\n", file_path);

    return 0;
}

