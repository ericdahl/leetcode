int find_magnitude(int x) {
    int mag = 1;
    for (int t = x; t >= 10; t /= 10) {
        mag *= 10;
    }
    return mag;
}

int reverse(int x){

    if (x == INT_MIN) {
        // can't abs this, but also too large to reverse anyways
        return 0;
    }

    bool is_positive = (x > 0);
    if (!is_positive) {
        x = abs(x);
    }

    int mag = find_magnitude(x);

    int r = 0;
    for (; x > 0; x /= 10, mag /= 10) {

        if ((x % 10) > INT_MAX / mag) {
            return 0;
        }
        if (r > INT_MAX - (x % 10) * mag) {
            return 0;
        }

        r += (x % 10) * mag;
    }

    if (!is_positive) r *= -1;

    return r;
}