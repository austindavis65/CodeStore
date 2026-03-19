#include "wordle.h"
#include <string.h>

int score(char **word_list, char *candidate, guess *prior_guesses, int num_prior_guesses) {
    int total_score = 0;

    for (int i = 0; word_list[i] != NULL; i++) {
        if (!is_viable_candidate(word_list[i], prior_guesses, num_prior_guesses)) {
            continue;
        }

        char word_copy[6];
        strcpy(word_copy, word_list[i]);

        int word_score = 0;

        for (int j = 0; j < 5; j++) {
            if (candidate[j] == word_copy[j]) {
                word_score += EXACT_HIT_POINTS;
                word_copy[j] = '_'; // Cross off matched letter
            }
        }

        for (int j = 0; j < 5; j++) {
            for (int k = 0; k < 5; k++) {
                if (word_copy[k] != '_' && candidate[j] == word_copy[k] && j != k) {
                    word_score += PARTIAL_HIT_POINTS;
                    word_copy[k] = '_'; // Cross off matched letter
                    break; // Don't count same letter twice
                }
            }
        }

        total_score += word_score;
    }

    return total_score;
}
