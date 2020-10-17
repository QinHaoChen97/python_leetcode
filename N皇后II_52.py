#!/usr/bin/python3
class Solution:
    def totalNQueens(self, n: int) -> int:
        def traceback(row:int)->int: #row为行数
            if n==row:
                return 1
            else:
                count=0
                for i in range(n):#i为列数
                    if i in columns or row-i in diagonal1 or row+i in diagonal2:
                        continue
                    else:
                        columns.add(i)
                        diagonal1.add(row-i)
                        diagonal2.add(row+i)
                        count += traceback(row+1)
                        columns.remove(i)
                        diagonal1.remove(row-i)
                        diagonal2.remove(row+i) 
                return count

        columns=set()
        diagonal1=set()
        diagonal2=set()
        return traceback(0)
if __name__ == "__main__":
    a=Solution()
    i=a.totalNQueens(4)
    print(i,flush=True)