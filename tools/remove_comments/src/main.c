#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define COMMENT_MARKER "1'"

void remove_comments(const char *input_file, const char *output_file) {
    FILE *input_fp = fopen(input_file, "r");
    FILE *output_fp = fopen(output_file, "w");

    if (input_fp == NULL || output_fp == NULL) {
        printf("Error al abrir el archivo origen.\n");
        exit(EXIT_FAILURE);
    }

    char line[256];

    while (fgets(line, sizeof(line), input_fp)) {
        // Buscar el índice del marcador de comentario
        char *comment_marker = strstr(line, COMMENT_MARKER);
        
        // Si se encuentra el marcador de comentario, omitir la línea
        if (comment_marker != NULL) {
            continue;
        }

        // Escribir la línea al archivo de salida
        fputs(line, output_fp);
    }

    fclose(input_fp);
    fclose(output_fp);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Uso: %s <archivo_entrada> <archivo_salida>\n", argv[0]);
        return EXIT_FAILURE;
    }

    const char *input_file = argv[1];
    const char *output_file = argv[2];

    remove_comments(input_file, output_file);

    printf("Comentarios eliminados con éxito en el archivo %s.\n", input_file);

    return EXIT_SUCCESS;
}