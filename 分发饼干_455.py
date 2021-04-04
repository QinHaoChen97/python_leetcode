#！/usr/bin/env python3
class Solution:
    def findContentChildren(self,g,s) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        count:int=0
        g_len= len(g)
        s_len= len(s)
        g_s=0
        s_s=0
        while g_s<g_len and s_s<s_len:
            if s[s_s]>=g[g_s]:
                count=count+1
                g_s=g_s+1
                s_s=s_s+1
            else:#尝试把这块饼干分给下一个胃口小的人
                g_s=g_s+1
        return  count

