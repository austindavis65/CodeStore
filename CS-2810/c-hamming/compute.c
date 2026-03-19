#include "compute.h"


#include <stddef.h>

int compute(char *first, char *second)
{
    if (!first || !second) {
        return -1;
    }

    const char *a = first;
    const char *b = second;
    
    while (*a && *b) {
        a++;
        b++;
    }
    
    if (*a || *b) {
        return -1;
    }
    
    a = first;
    b = second;
    
    int differences = 0;
    
    while (1) {
        char aa = *a;
        char bb = *b;
        
        if (!aa || !bb) {
            break;
        }
        
        if (aa != bb) {
            differences++;
        }
        
        a++;
        b++;
    }
    
    return differences;
}
