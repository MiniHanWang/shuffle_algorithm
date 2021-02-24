#@Time:2/24/202111:06 AM
#@Author: Mini(Wang Han)
#@Site:
#@File:test1.py
import random
#k=1
def reservoirSampling1(arr):
    # 初始化把第1个元素放进结果中
    res = arr[0]
    i = 1  # 从第2个元素开始考虑
    while i < len(arr):
        # 概率1/i选取第i个元素作为结果
        r = random.randint(0, i)
        if r == 0:
            res = arr[i]
        i += 1
    # 这样，遍历一遍就可以等概率的选择一个数输出
    return res
#k> 1
def reservoirSamplingk(arr, k):
    res = arr[:k]
    i = k
    while i < len(arr):
        # 以k/i的概率选取第i个元素，用来等概率的替换之前选中的1个元素
        r = random.randint(0, i)
        if r < k:  # 小于k的概率就是k/i，替换res中第r个已选中的数
            res[r] = arr[i]
        i += 1
    return res
arr=[1,2,4,1,4,2,3,4,7,9]
print(reservoirSamplingk(arr, 4))