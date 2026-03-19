#include <stdio.h>
#include "wordle.h"

guess parse_guess(char *input) {
    guess g;
    const char *cursor = input;

    for (int i = 0; i < 5; i++) {
        if (*cursor == '[') {
            g.letters[i] = *(cursor + 1);
            g.feedback[i] = EXACT_HIT;
            cursor += 3;
        } else if (*cursor == '(') {
            g.letters[i] = *(cursor + 1);
            g.feedback[i] = PARTIAL_HIT;
            cursor += 3;
        } else if (*cursor >= 'a' && *cursor <= 'z') {
            g.letters[i] = *cursor;
            g.feedback[i] = MISS;
            cursor += 1;
        } else {
            fprintf(stderr, "Invalid input format\n");
            g.letters[i] = '\0';
            g.feedback[i] = MISS;
            return g;
        }
    }

    g.letters[5] = '\0';

    return g;
}
