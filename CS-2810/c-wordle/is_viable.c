#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include "wordle.h"

bool is_viable_candidate(char *candidate, guess *guesses, int guess_count) {
    for (int g = 0; g < guess_count; g++) {
        char copy[6];
        strcpy(copy, candidate);

        for (int i = 0; i < 5; i++) {
            if (guesses[g].feedback[i] == EXACT_HIT) {
                if (copy[i] != guesses[g].letters[i]) {
                    return false;
                }
                copy[i] = '_';
            }
        }

        for (int i = 0; i < 5; i++) {
            if (guesses[g].feedback[i] == PARTIAL_HIT) {
                if (copy[i] == guesses[g].letters[i]) {
                    return false;
                }
            }
        }

        for (int i = 0; i < 5; i++) {
            if (guesses[g].feedback[i] == PARTIAL_HIT) {
                bool found = false;
                for (int j = 0; j < 5; j++) {
                    if (copy[j] == guesses[g].letters[i]) {
                        copy[j] = '_';
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    return false;
                }
            }
        }

        for (int i = 0; i < 5; i++) {
            if (guesses[g].feedback[i] == MISS) {
                for (int j = 0; j < 5; j++) {
                    if (copy[j] == guesses[g].letters[i]) {
                        return false;
                    }
                }
            }
        }
    }

    return true;
}
