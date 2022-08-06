static int index_of(char c, char* start, char* end) {
    for (char* i = start; i < end; ++i) {
        if (c == *i) {
            return i - start;
        }
    }
    return -1;
}

int lengthOfLongestSubstring(char * s){
    int longest = 0;
    char* start = s;
    char* end = s;

    for (char* c = s; *c; ++c) {

        int i = index_of(*c, start, end);
        if (i >= 0) {
            start += i + 1;
        }
        ++end;

        if (end - start > longest) {
            longest = end - start;
        }

    }

    return longest;

}