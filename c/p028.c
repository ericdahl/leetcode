int strStr(char * haystack, char * needle){

    for (const char* c = haystack; *c; ++c) {
        for (const char* n = needle; *n && *n == *(c + (n - needle)); ++n) {
            if (*(n + 1) == NULL) {
                return c - haystack;
            }
        }
    }

    return -1;
}