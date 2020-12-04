class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(start, start+(n*2), 2):
            res = res ^ i
        return res

def main():
    a = Solution()
    # a.xorOperation(5, 0)
    # print()
    # a.xorOperation(4, 3)
    print(a.xorOperation(5, 0))
    print(a.xorOperation(4, 3))
    print(a.xorOperation(1, 7))
    print(a.xorOperation(10, 5))

if __name__ == "__main__":
    main()