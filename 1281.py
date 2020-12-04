class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ints = [int(s) for s in str(n)]
        prod = 1
        for i in ints:
            prod = prod * i
        return prod-sum(ints)
        
def main():
    a = Solution()
    print(a.subtractProductAndSum(234))
    print(a.subtractProductAndSum(4421))

if __name__ == "__main__":
    main()