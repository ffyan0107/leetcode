"""
  author：ffyan0107
  date:  2019-12-23
  description: two sum
"""

class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i


def main():
    array = [2, 12, 11, 7]
    target = 9
    result = Solution()
    index = result.twoSum(array, target)
    print(index)

if __name__ == "__main__":
    main()

