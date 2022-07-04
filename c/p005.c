static bool is_palindrome(const char* s, const int len) {
    const char* left = s;
    const char* right = s + len - 1;

    for (; left < right; ++left, --right) {
        if (*left != *right) {
            return false;
        }
    }

    return true;
}

char * longestPalindrome(char * s){

    const int s_len = strlen(s);
    const char* s_end = s + s_len;

    for (int window_size = s_len; window_size > 0; --window_size) {
        for (char* start = s; start + window_size <= s_end; ++start) {

            if (is_palindrome(start, window_size)) {
                if (start + window_size <= s_end) {
                    // probably shouldn't be altering the input..
                   *(start + window_size) = NULL;
                }
                return start;
            }
        }
    }

    return NULL;
}