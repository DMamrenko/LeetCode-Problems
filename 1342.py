class Solution:
    def numberOfSteps (self, num: int) -> int:
        even = lambda x : x % 2 == 0
        steps = 0
        while num != 0:
            if even(num):
                num /= 2
                steps += 1
            else:
                num -= 1
                steps += 1
        return steps

def main():
    a = Solution()
    print(a.numberOfSteps(14))
    print(a.numberOfSteps(8))
    print(a.numberOfSteps(123))

if __name__ == "__main__":
    main()