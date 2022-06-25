// TODO: can be O(N) if using a stack
int longestValidParentheses(char * s){

    int longest = 0;

    for (const char* c = s; *c; ++c) {

        int open_count = 0;

        for (const char* j = c; *j; ++j) {

            if (*j == '(') open_count++;
            else if (*j == ')') --open_count;

            if (open_count == 0 && j - c > longest) {
                longest = j - c + 1;
            } else if (open_count < 0) {
                break;
            }

        }
    }
    return longest;

}