#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_LINE 256

int is_numeric(const char *s) {
    for (int i = 0; s[i]; i++) {
        if (!isdigit(s[i]) && s[i] != '.') {
            return 0;
        }
    }
    return 1;
}

void update_or_add_value(const char *filename, const char *key, const char *value) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        fprintf(stderr, "Error: no se pudo abrir el archivo.\n");
        return;
    }

    FILE *temp = fopen("temp.txt", "w");
    if (!temp) {
        fclose(file);
        fprintf(stderr, "Error: no se pudo crear el archivo temporal.\n");
        return;
    }

    char line[MAX_LINE];
    int key_found = 0;

    while (fgets(line, sizeof(line), file)) {
        char *equal_pos = strchr(line, '=');
        if (equal_pos) {
            char key_in_file[MAX_LINE];
            strncpy(key_in_file, line, equal_pos - line);
            key_in_file[equal_pos - line] = '\0'; // null-terminate the key string

            if (strcmp(key_in_file, key) == 0) {
                // Reemplazar la línea con la nueva key-value
                key_found = 1;
                if (is_numeric(value)) {
                    fprintf(temp, "%s=%s\n", key, value);
                } else {
                    fprintf(temp, "%s=\"%s\"\n", key, value);
                }
            } else {
                // Escribir la línea original
                fputs(line, temp);
            }
        } else {
            // En caso de que la línea no contenga '=' (cualquier anomalía)
            fputs(line, temp);
        }
    }

    if (!key_found) {
        // Añadir el key-value al final si no se encuentra
        if (is_numeric(value)) {
            fprintf(temp, "%s=%s\n", key, value);
        } else {
            fprintf(temp, "%s=\"%s\"\n", key, value);
        }
    }

    fclose(file);
    fclose(temp);

    // Reemplazar el archivo original por el temporal
    remove(filename);
    rename("temp.txt", filename);
}

int main(int argc, char *argv[]) {
    if (argc < 4) {
        fprintf(stderr, "Uso: %s <nombre_archivo> <key> <value>\n", argv[0]);
        return 1;
    }

    const char *filename = argv[1];
    const char *key = argv[2];
    const char *value = argv[3];

    update_or_add_value(filename, key, value);

    return 0;
}