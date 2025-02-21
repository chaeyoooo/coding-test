def solution(nums):
    #그니까 nums배열이 있는데 set으로 해서 갯수를 셈 근데 그 갯수가 num //2 보다 크면 num//2 값 출력
    # 만약 아니면 그냥 set의 갯수를 출력 하면 됨
    range_nums = set(nums)
    if len(range_nums) > len(nums) // 2:
        return len(nums) //2
    return len(range_nums)
