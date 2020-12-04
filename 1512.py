class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    result += 1
        return result

def main():
    e1 = [1,2,3,1,1,3]
    e2 = [1,1,1,1]
    e3 = [1,2,3]

    a = Solution()
    a.numIdenticalPairs(e1)
    a.numIdenticalPairs(e2)
    a.numIdenticalPairs(e3)
    
if __name__ == "__main__":
    main()