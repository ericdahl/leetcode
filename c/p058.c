int lengthOfLastWord(char * s){

    int len = 0;
    int last_len = 0;

    for (const char* c = s; *c; ++c) {

        if (*c != ' ') {
            ++len;
            last_len = len;
        } else {
            len = 0;
        }

    }
    return last_len;
}