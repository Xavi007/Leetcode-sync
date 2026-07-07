int removeElement(int* nums, int numsSize, int val) {
    int count = 0;

    for(int x = 0; x < numsSize; ++x)
    {
        if (nums[x] != val)
        {
            nums[count] = nums[x];
            count += 1;
        }
    }
    return count;
}