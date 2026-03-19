#include <stdio.h>
#include "solve.h"

// write your code here
// note that solve.h is included. Look at that file
// to see what values are already defined for you and
// what your function signatures should match. You do not
// need to copy anything from main.c or solve.h into this file.


void print_maze(char field[SIZE_Y][SIZE_X]) {
    for (int y = 0; y < SIZE_Y; y++) {
        for (int x = 0; x < SIZE_X; x++) {
            putchar(field[y][x]);
        }
        putchar('\n');
    }
}

void solve_maze(char field[SIZE_Y][SIZE_X]) {
    int changes;
    do {
        changes = 0;
        // Scan the field (excluding borders)
        for (int y = 1; y < SIZE_Y - 1; y++) {
            for (int x = 1; x < SIZE_X - 1; x++) {
                // Only check path positions
                if (field[y][x] != '.') {
                    continue;
                }
                
                // Count wall neighbors
                int wall_count = 0;
                if (field[y-1][x] == '@') wall_count++;  // Up
                if (field[y+1][x] == '@') wall_count++;  // Down
                if (field[y][x-1] == '@') wall_count++;  // Left
                if (field[y][x+1] == '@') wall_count++;  // Right
                
                // If this is a dead end (3 walls), fill it
                if (wall_count == 3) {
                    field[y][x] = '@';
                    changes++;
                }
            }
        }
    } while (changes > 0);
}
