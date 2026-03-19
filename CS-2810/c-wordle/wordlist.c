#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "wordle.h"

char **read_word_list(char *filename) {
    size_t capacity = 32;
    size_t length = 0;

    char **word_list = malloc(capacity * sizeof(char *));
    if (word_list == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }

    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        fprintf(stderr, "Could not open file %s\n", filename);
        free(word_list);
        return NULL;
    }

    char line[16];

    while (fgets(line, sizeof(line), fp) != NULL) {
        if (strlen(line) != 6 || line[5] != '\n') {
            fprintf(stderr, "Invalid word format: %s", line);
            for (size_t i = 0; i < length; i++) {
                free(word_list[i]);
            }
            free(word_list);
            fclose(fp);
            return NULL;
        }

        if (length >= capacity) {
            capacity *= 2;
            char **temp = realloc(word_list, capacity * sizeof(char *));

            if (temp == NULL) {
                fprintf(stderr, "Memory reallocation failed\n");
                for (size_t i = 0; i < length; i++) {
                    free(word_list[i]);
                }
                free(word_list);
                fclose(fp);
                return NULL;
            }
            word_list = temp;
        }

        word_list[length] = malloc(6 * sizeof(char));

        strncpy(word_list[length], line, 5);
        word_list[length][5] = '\0';

        length++;
    }

    fclose(fp);

    if (length >= capacity) {
        capacity++;
        char **temp = realloc(word_list, capacity * sizeof(char *));
        if (temp == NULL) {
            fprintf(stderr, "Memory reallocation failed\n");
            for (size_t i = 0; i < length; i++) {
                free(word_list[i]);
            }
            free(word_list);
            return NULL;
        }
        word_list = temp;
    }
    word_list[length] = NULL;

    return word_list;
}

void free_word_list(char **word_list) {
    if (word_list == NULL) {
        return;
    }

    for (int i = 0; word_list[i] != NULL; i++) {
        free(word_list[i]);
    }

    free(word_list);
}
