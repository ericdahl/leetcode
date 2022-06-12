int myAtoi(char * s){
    // ignore whitespace
    for (; *s == ' '; ++s);

    // step 2 - negative/positive
    const bool is_negative = (*s == '-');
    if (*s == '-' || *s == '+') ++s;

    int result = 0;
    for (char* c = s; *c && isdigit(*c); ++c) {

        // skip multiplying by 10 on first digit
        if (c != s) {
            if (result > INT_MAX / 10) {
                return is_negative ? INT_MIN : INT_MAX;
            }
            result *= 10;
        }

        if (result > INT_MAX - (*c - '0')) {
            return is_negative ? INT_MIN : INT_MAX;
        }
        result += (*c - '0');
    }

    if (is_negative) result *= -1;

    return result;
}