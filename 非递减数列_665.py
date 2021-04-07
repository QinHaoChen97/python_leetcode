'''
给你一个长度为n的整数数组，请你判断在最多改变1个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的：对于数组中任意的i(0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

'''
# ! /usr/bin/env python3

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:  # 必定可以满足的情况
            return True

        deminish: int = 0  # 记录需要处理的次数

        # 第一个位置需要单独处理
        if nums[0] > nums[1]:
            nums[0] = nums[1]
            deminish += 1

        for i in range(2, len(nums)):  # 因为已经做了预处理，直接从第二个位置开始

            if nums[i] < nums[i - 1]:
                '''
                当出现不符合升序的节点时，最好的做法是让前一节点的值等于当前节点的值，即nums[i-1]=nums[i](可以只在逻辑上这样                    认为而不实际进行操作),这是贪心策略

                但这需要满足i-2个节点的值小于等于当前节点
                否则 只能使nums[i]=nums[i-1]
                '''

                deminish += 1  # 记录修改
                if deminish == 2:
                    return False
                if nums[i] >= nums[i - 2]:  # 可以啥都不用干，我们自己在逻辑中认为修改了nums[i-1]=nums[i]
                    # 这里不用判断i-2是否越界是因为我们在上文中先对开头做了预处理
                    pass
                else:
                    nums[i] = nums[i - 1]

        return True