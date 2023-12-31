#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include "include/libxml/tree.h"
#include "include/libxml/parser.h"
#include "include/libxml/xmlregexp.h"

#define SIZE 1000

void harness(char* buffer, ssize_t length) {
	// your code here
	if (length <= 0 || length >= SIZE) {
        return;
	}
	else {
		buffer[length] = '\0'; //add terminator
		xmlRegexpPtr comp = xmlRegexpCompile((const xmlChar *)buffer);
		if (comp == NULL) {
			return;
		}
		else {
			xmlRegFreeRegexp(comp); // Free memory
			return;
		}
	}
}

int main(int argc, char** argv) {
	char input[SIZE];
	while (__AFL_LOOP(1000)) {
		ssize_t length = read(STDIN_FILENO, input, SIZE);
		harness(input, length);
	}
	return 0;
}
