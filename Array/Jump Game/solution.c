bool canJump(int* nums, int numsSize) {
    int target = numsSize-1;

    for(int i = numsSize-1; i > -1 ; --i)
    {
        if ((i + nums[i]) >= target)
        {
            target = i;
        }
    }
    return (target == 0);
}