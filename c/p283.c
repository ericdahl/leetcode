static void swap(int* a, int* b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void moveZeroes(int* nums, int numsSize){

    int j = 0;

    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != 0) {
            swap(nums + i, nums + j);
            ++j;
        }
    }

}
