'''
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

示例：
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
'''

# 解题思路：扫描一遍字符串，用一个字典记录各个字母出现的频率
# 再扫描一遍字符串
# 每次一组字符串的累计频率降为0时则分行

#上述做法可以进行简化，具体见https://leetcode-cn.com/problems/partition-labels/solution/hua-fen-zi-mu-qu-jian-by-leetcode-solution/
#改用每个字母最后一次出现的坐标位置来代替统计频率


from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return [0]
        appear_time: dict = {}  # 统计字母出现频率
        for letter in S:
            if letter not in appear_time:
                appear_time[letter] = 1
            else:
                appear_time[letter] += 1

        return_List = []
        a_partition: list = []
        partition_count: int = 0  # 当partition=0时则分出了一个数组
        partition_long: int = 0  # 一个片区的长度

        for letter in S:
            partition_long += 1  # 片区长度+1

            if letter not in a_partition:
                a_partition.append(letter)
                partition_count += appear_time[letter]

            partition_count -= 1  # 无论如何都会减去一个频次

            if partition_count == 0:
                return_List.append(partition_long)
                partition_long = 0
                a_partition.clear()

        return return_List
