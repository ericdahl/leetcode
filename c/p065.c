bool is_integer(const char* s) {
    if (*s == '-' || *s == '+') ++s;

    int digits = 0;
    for (const char* c = s; *c; ++c) {
        if (!isdigit(*c)) return false;
        ++digits;
    }

    return digits > 0;
}

bool is_decimal(const char* s) {
    if (*s == '-' || *s == '+') ++s;

    const char* dot = NULL;
    for (const char* c = s; *c; ++c) {

        if (*c == '.') {
            // already found a dot, can't have multiple
            if (dot) {
                return false;
            }
            dot = c;
            continue;
        }

        if (!isdigit(*c)) return false;
    }

    if (!dot) return false;
    if (dot == s) return is_integer(s + 1);

    return true;
}

bool isNumber(char * s){

    char* e = NULL;
    for (const char* c = s; *c; ++c) {
        if (*c == 'e' || *c == 'E') {
            e = c;
            break;
        }
    }

    if (!e) {
        return is_integer(s) || is_decimal(s);
    } else {
        *e = NULL; // ick.. modifying input. Probably shouldn't do that
        return (is_integer(s) || is_decimal(s)) && is_integer(e +1);
    }
}