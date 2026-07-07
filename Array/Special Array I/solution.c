bool isArraySpecial(int* nums, int numsSize) {
    char arr[numsSize];
    memset(arr, -1, numsSize);
    
    if (numsSize <= 1)
    {
        return true;
    }

    for (int i =0; i < numsSize; i++)
    {
        if ((nums[i] % 2) == 0)
        {
            arr[i] = 0;
        }
        else
        {
            arr[i] = 1;
        }
    }
    for (int i = 0; i < numsSize-1; i++)
    {
        if (arr[i] == arr[i+1])
        {
            return false;
        }
    }
    return true;
}