class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = [0]*len(indices)
        for index, number in enumerate(indices):
            result[number] = s[index]
        return ''.join(result)

def main():
    a = Solution()
    print(a.restoreString("codeleet", [4,5,6,7,0,2,1,3]))
    print(a.restoreString("abc", [0,1,2]))
    print(a.restoreString("aiohn", [3,1,4,2,0]))
    print(a.restoreString("aaiougrt", [4,0,2,6,7,3,1,5]))
    print(a.restoreString("art", [1,0,2]))

if __name__ == "__main__":
    main()