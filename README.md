# shuffle_algorithm
水库抽样算法——一个亚线性空间算法
输入：一组数据，其大小未知
输出：这组数据的k个均匀抽样
要求/实现结果：
	进扫描数据一次
	空间复杂性为O（k）
	扫描到数据的前n个数字时，（n>k），保存当前已经扫描数据的k个均匀抽样

算法主要思想：
	申请一个长度为k的数组A保存抽样
	保存首先接收到的k个元素
	当接受到第i个新元素t时，以k/i的概率来随机替换A中的元素（即，生成[1，i]间随机数j，若j≤k,则以t替换A[j]）

算法公式
k/i×(1-k/(i+1)×1/k)×(1-k/(i+2)×1/k)×⋯×(1-k/n×1/k)=k/n

 
Python 代码实现
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

结果：
[2, 9, 4, 1]
