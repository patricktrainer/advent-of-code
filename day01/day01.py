
with open('input.txt', 'r') as f:
    nums = [int(line.strip()) for line in f]

def sum_nums(nums):
    sum_nums = []
    while len(nums) > 2:
        sum_nums.append(sum(nums[0:3]))
        nums.remove(nums[0])

    return sum_nums


def compare_nums(nums):
    gt = 0
    for i, num in enumerate(nums):
        if num > nums[i - 1]:
            gt += 1
    return gt


nums = sum_nums(nums)
compare_nums(nums)
