// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {

    if (n == 1) return 1;

    int left = 1;
    int right = n;

    while (true) {
        if (right == left + 1) {
            if (isBadVersion(right) && !isBadVersion(left)) {
                return right;
            }
            return left;
        }

        const int middle = left + (right - left) / 2;

        if (isBadVersion(middle)) {
            right = middle;
        } else {
            left = middle;
        }

    }
}