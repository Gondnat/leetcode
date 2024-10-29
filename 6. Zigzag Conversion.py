class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ''
        array = [['' for _ in range(len(s))] for _ in range(numRows)]
        j = 0
        k = 0
        while k < len(s):
            if j%(numRows-1) == 0:
                for i in range(numRows):
                    if k + i >= len(s):
                        break
                    array[i][j] = s[k+i]
                k += numRows
            else:
                array[numRows-1-j%(numRows-1)][j] = s[k]
                k += 1
            j += 1

        for i in range(numRows):
            for j in range(len(s)):
                if array[i][j] != '':
                    res += array[i][j]
        return res

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    sol = Solution()
    print(sol.convert(s, numRows))