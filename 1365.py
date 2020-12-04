class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sor = sorted(nums)
        result = [sor.index(num) for num in nums]
        return result

def main():
    a = Solution()
    print(a.smallerNumbersThanCurrent([8,1,2,2,3]))

if __name__ == "__main__":
    main()