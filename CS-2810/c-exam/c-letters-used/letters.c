#include "letters.h"
#include <stdio.h>
#include <ctype.h>

void letters_used(char *line) {
    int letter_count[26] = {0}; // Initialize an array to count occurrences of each letter

    // Iterate through the line, counting occurrences of each letter
    while (*line) {
        if (isalpha(*line)) {
            int index = tolower(*line) - 'a';
            letter_count[index]++;
        }
        line++;
    }

    // Print the letters that were used
    for (int i = 0; i < 26; i++) {
        if (letter_count[i] > 0) {
            printf("%c", 'a' + i);
        }
    }
    printf("\n");
}
