#include <stdio.h>


void print_diamond(int size){
	// if (size == 1){
	// 	putchar('*');
	// 	putchar('\n');
	// 	return;
	// }
	int spaces = size;
	char star[1000] = "*";
	int end = 1;
	while (spaces != 0){
		char str[1000] = "";
		for(int i = 0; i < (spaces - 1); i++){
			char space = ' ';
			str[i] = space;
		}
		

		printf("%s",str);
		printf("%s",star);
		putchar('\n');
		star[end] = '*';
		end = end + 1;
		star[end] = '*';
		end = end + 1;
		spaces--;

	}
	
	end = end - 1;
	star[end] = '\0';
	end = end - 1;
	star[end] = '\0';

	spaces = 0;
	int count = 0;
	while (spaces != (size - 1)){
		char str[1000] = "";
		for(int i = 0; i < (count + 1); i++){
			char space = ' ';
			str[i] = space;

		}
		
		count++;
		printf("%s",str);
		end = end - 1;
		star[end] = '\0';
		end = end - 1;
		star[end] = '\0';
		printf("%s",star);
		putchar('\n');
		spaces++;	
	}
}
