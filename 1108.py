class Solution:
    def defangIPaddr(self, address: str) -> str:
        parts = address.split('.')
        return "[.]".join(parts)

def main():
    a = Solution()
    b = a.defangIPaddr("1.1.1.1")
    print(b)

if __name__ == "__main__":
    main()