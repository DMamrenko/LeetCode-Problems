class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for letter in S:
            if letter in J:
                result += 1
        return result

def main():
    a = Solution()
    print(a.numJewelsInStones("aA", "aAAbbbb"))
    print(a.numJewelsInStones("z", "ZZ"))
    

if __name__ == "__main__":
    main()

