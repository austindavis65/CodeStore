#include "wordle.h"
#include <stdio.h>
#include <string.h>

struct recommendation {
    int score;
    char word[6];
};

void recommend(char **word_list, guess *guesses, int guess_count) {
    struct recommendation recs[RECOMMENDATION_COUNT + 1];
    int count = 0;  // Track number of recommendations
    
    for (int i = 0; word_list[i] != NULL; i++) {
        if (!is_viable_candidate(word_list[i], guesses, guess_count)) {
            continue;
        }
        
        int word_score = score(word_list, word_list[i], guesses, guess_count);
        
        strcpy(recs[count].word, word_list[i]);
        recs[count].score = word_score;
        
        int j = count;
        while (j > 0) {
            if (recs[j].score > recs[j-1].score || 
                (recs[j].score == recs[j-1].score && 
                 strcmp(recs[j].word, recs[j-1].word) < 0)) {
                struct recommendation temp = recs[j];
                recs[j] = recs[j-1];
                recs[j-1] = temp;
                j--;
            } else {
                break;  
            }
        }
        
        if (count < RECOMMENDATION_COUNT) {
            count++;
        }
    }
    
    for (int i = 0; i < count; i++) {
	printf("%d: %s\n", recs[i].score, recs[i].word);
    }
}
