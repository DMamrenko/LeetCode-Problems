class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)//2):
            result.extend(nums[2*i]*[nums[(2*i)+1]])
        return result
            
def main():
    a = Solution()
    print(a.decompressRLElist([1,2,3,4]))
    print(a.decompressRLElist([1,1,2,3]))

if __name__ == "__main__":
    main()