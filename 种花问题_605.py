#! /usr/bin/env python3
'''
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数n ，
能否在不打破种植规则的情况下种入n朵花？能则返回 true ，不能则返回 false。
示例 1：

输入：flowerbed = [1,0,0,0,1], n = 1
输出：true
示例 2：

输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
'''
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # new_flowerbed: List[int] = [0, flowerbed[0:], 0] 这么写会变成在里面插入了一个数组
        # 构建一个新的列表，让首尾的判断规则也可以满足每连续三个空则在三个空位的中心插入一朵花
        new_flowerbed: List[int] = [0] + flowerbed + [0]
        count_empty: int = 0
        count_insert: int = 0
        for bed in new_flowerbed:
            if bed == 0:
                count_empty += 1
                if count_empty == 3:
                    count_insert += 1
                    count_empty = 1  # 在三个空格的中间空格插入花之后，第三个位置已经是一个空格了，所以要置1不是置0
            else:
                count_empty = 0

        if count_insert >= n:  # 这里是大于等于不是等于，少种也是可以的
            return True

        return False


if __name__ == '__main__':
    flowerbed = [1, 2, 3]
    new_flowerbed: List[int] = [0, flowerbed[0:], 0]
    print(new_flowerbed)
