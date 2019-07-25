https://www.jianshu.com/p/bbbab7fa77a2
class SortDemo():
    def findMinAndMin(self,L):
        if len(L)<1:
            return (None,None)
        # new_L = self.BubbleSort(L)
        # new_L = self.SelectionSort(L)
        # new_L = self.InsertionSort(L)
        new_L = self.ShellSort(L)
        ret_set = (new_L[0],new_L[-1])
        return ret_set

    def BubbleSort(self,L):
        """
        冒泡排序
        :param L:
        :return:
        """
        for i in range(len(L)-1):
            for j in range(len(L) - i - 1):
                if L[j]>L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
        return L

    def SelectionSort(self,L):
        """
        选择排序
        :param L:
        :return:
        """
        for i in range(len(L) - 1):
            minIndex = i
            for j in range(i + 1,len(L)):
                if L[j]<L[minIndex]:   # 更新最小值索引
                    minIndex = j
            L[i], L[minIndex] = L[minIndex], L[i]   # 把最小数交换到前面
        return L

    def InsertionSort(self,L):
        """
        插入排序
        :param L:
        :return:
        """
        for i in range(len(L)-1):
            curNum, PreIndex = L[i+1], i # curNum 保存当前待插入的数
            while PreIndex >= 0 and curNum < L[PreIndex]:  # 将比 curNum 大的元素向后移动
                L[PreIndex + 1] = L[PreIndex]
                PreIndex -= 1
            L[PreIndex + 1] = curNum # 待插入的数的正确位置
        return L

    def ShellSort(self,L):
        """
        希尔排序，分而治之的思想结合插入排序，{4,1}这样的现在排好一个子序列，对子序列内部进行排序，在进行迭代
        经过前几次排序，序列已经基本有序，因此此次排序时间效率就提高了很多
        :param L:
        :return:
        """
        lens = len(L)
        print(lens)
        gap = 1
        while gap < lens // 3:
            gap = gap * 3 +1  # 动态定义间隔序列
            print(gap)
        while gap > 0 :
            print(range(gap,lens))
            for i in range(gap,lens):
                curNum, PreIndex = L[i], i - gap  # curNum 保存当前待插入的数,gap是补长
                while PreIndex >= 0 and curNum < L[PreIndex]:  # 将比 curNum 大的元素向后移动
                    L[PreIndex + gap] = L[PreIndex]
                    PreIndex -= gap
                L[PreIndex + gap] = curNum # 待插入的数的正确位置
            gap //= 3 # 下一个动态间隔
        return L

if __name__ == "__main__":
    L = [21,4,13,55,23,44,56,7,39]
    sort = SortDemo()
    ret_data = sort.findMinAndMin(L)
    print(ret_data)
