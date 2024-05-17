#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <sys/statvfs.h>

#define MAX_FILES 1024

typedef struct {
    char name[256];
    char ext[256];
    int size;
    int is_dir;
} Item;

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Por favor, proporciona un directorio.\n");
        return 1;
    }

    char *directory = argv[1];
    DIR *dir = opendir(directory);

    if (dir == NULL) {
        printf("Error: '%s' no es un directorio válido.\n", directory);
        return 1;
    }

    Item items[MAX_FILES];
    int items_count = 0;

    struct dirent *entry;
    struct stat file_stat;
    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }

        char filename[256];
        sprintf(filename, "%s/%s", directory, entry->d_name);
        
        if (stat(filename, &file_stat) < 0) {
            printf("Error al obtener información de %s\n", entry->d_name);
            continue;
        }
        
        if (entry->d_type == DT_DIR) {
            strcpy(items[items_count].name, entry->d_name);
            strcpy(items[items_count].ext, "     ");
            items[items_count].size = 0;
            items[items_count].is_dir = 1;
            items_count++;
        } else {
            char *dot = strrchr(entry->d_name, '.');
            if (dot) {
                strncpy(items[items_count].name, entry->d_name, dot - entry->d_name);
                items[items_count].name[dot - entry->d_name] = '\0';
                strcpy(items[items_count].ext, dot);
            } else {
                strcpy(items[items_count].name, entry->d_name);
                strcpy(items[items_count].ext, ".   ");
            }
            int size_kb = 0;
            if (!S_ISDIR(file_stat.st_mode)) {
                size_kb = (file_stat.st_size + 1023) / 1024;
                if (size_kb == 0) {
                    size_kb = 1;
                }
            }
            items[items_count].size = size_kb;
            items_count++;
        }
    }

    closedir(dir);

    printf("\nDrive C:/\n\n");

    for (int i = 0; i < items_count; i++) {
        if (items[i].is_dir) {
            printf(">%-8s%-5s     ", items[i].name, items[i].ext);
        } else {
            printf("%-8s%-5s %4dK", items[i].name, items[i].ext, items[i].size);
        }
        if (i % 2 != 0) {
            printf("\n");
        } else {
            printf("    ");
        }
    }
    if (items_count % 2 != 0) {
        printf("\n");
    }

    struct statvfs stat;
    if (statvfs(directory, &stat) != 0) {
        printf("Error al obtener el espacio libre en el disco.\n");
        return 1;
    }
    unsigned long free_space_kb = stat.f_bavail * stat.f_bsize / 1024;
    printf("\n%luK free\n", free_space_kb);

    return 0;
}