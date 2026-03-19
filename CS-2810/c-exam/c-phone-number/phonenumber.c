#include "phonenumber.h"

#include <stdio.h>
#include <ctype.h>
#include <string.h>

void format_phone_number(char *line) {
    int i = 0;
    char area_code[4] = {0};   // Space for 3 digits + null terminator
    char prefix[4] = {0};      // Space for 3 digits + null terminator
    char line_num[5] = {0};    // Space for 4 digits + null terminator
    int digits_found = 0;
    
    // Skip leading non-digits
    while (line[i] && !isdigit(line[i])) {
        i++;
    }
    
    // Get area code (3 digits)
    if (isdigit(line[i]) && isdigit(line[i+1]) && isdigit(line[i+2])) {
        area_code[0] = line[i];
        area_code[1] = line[i+1];
        area_code[2] = line[i+2];
        i += 3;
        digits_found += 3;
    } else {
        printf("Invalid input\n");
        return;
    }
    
    // Skip non-digits between area code and prefix
    while (line[i] && !isdigit(line[i])) {
        i++;
    }
    
    // Get prefix (3 digits)
    if (isdigit(line[i]) && isdigit(line[i+1]) && isdigit(line[i+2])) {
        prefix[0] = line[i];
        prefix[1] = line[i+1];
        prefix[2] = line[i+2];
        i += 3;
        digits_found += 3;
    } else {
        printf("Invalid input\n");
        return;
    }
    
    // Skip non-digits between prefix and line number
    while (line[i] && !isdigit(line[i])) {
        i++;
    }
    
    // Get line number (4 digits)
    if (isdigit(line[i]) && isdigit(line[i+1]) && 
        isdigit(line[i+2]) && isdigit(line[i+3])) {
        line_num[0] = line[i];
        line_num[1] = line[i+1];
        line_num[2] = line[i+2];
        line_num[3] = line[i+3];
        i += 4;
        digits_found += 4;
    } else {
        printf("Invalid input\n");
        return;
    }
    
    // Skip trailing non-digits
    while (line[i] && !isdigit(line[i])) {
        i++;
    }
    
    // Check if we've reached the end and found exactly 10 digits
    if (line[i] != '\0' || digits_found != 10) {
        printf("Invalid input\n");
        return;
    }
    
    // Print formatted phone number
    printf("(%s) %s-%s\n", area_code, prefix, line_num);
}
