# -*- coding:UTF-8 -*-
'''
立方：
2**3 ==8

break：
for i in range(3,11):
    if i % 2 == 0:
       break
else :# 未跳出循環的情況
    print(i)

時間：
time.strftime('format',time.localtime())
%Y-%m-%d %H-%M-%S

sort()：
列表函數，從小到大排列

format()：
3.1465926 	{:.2f}  => 3.15    # 小數2位
2.71        {:.0f}  =>    3    # 小數0位
5           {:0>2d} =>   05    # 整數2位,左補0
5           {:x<2d} =>   5x    # 整數2位,右補x
5           {:>2d}  =>    5    # 整數2位,左補寬度
5           {:<2d}  =>   5     # 整數2位,右補寬度

range()= list(xrange());
range(1,3) = [1,2]
xrange(1,3) =  xrange(1,3)
list(xrange(1,3)) = [1,2]

ord()：
chr()類型函數，返回ascll值

stdout.write():
stdout.write('\n') 等價于 print()
'''

from sys import stdout
n = 0
for n in range(4):
    x = 2*n+1
    y = 3- n
    stdout.write(' '* y + '*'* x+'\n')
    #print()
    if x ==7:
        for k in range(3):
            x -= 2
            y +=1
            print(' '*y+'*' * x)







''''
⭐⭐⭐⭐⭐⭐⭐⭐

# 求所有因子之和
def fenjie(x):
    num = 2
    sum = 1
    y = x
    list = [1]
    while num < y:
        if y % num == 0:  # 能被num整除就分解
            #y /= num
            sum = sum + num
            list.append(num)
            num += 1
        else:
            num += 1
    if x == sum:
        print(x)
        print(list)

#判斷素數和偶數
def sushu(x):
    for i in range(2,x):
        if x%i==0:
            return x
            break
    else:
        pass

# 判斷因子和與素數本身相等的數
if __name__ == '__main__':
    for x in range(2,1001):
        if sushu(x) != None:
           val = sushu(x)
           fenjie(val)
'''




