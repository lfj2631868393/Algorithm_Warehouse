"""
汉诺塔问题：
递归的经典问题之一
将n个圆盘由小到大，从上往下，依次放到圆柱上
三组圆柱
将它们移动到另一个圆柱上，并且保持原来的由小到大，从上往下
"""


# 汉诺塔:
def hanoi(n, a, b, c):  # n个圆盘，从a经过b到c
    if n > 0:
        hanoi(n - 1, a, c, b)  # 将n-1个圆盘从a到c再到b
        print('%d moving from %s to %s' % (n, a, c))  # 最下面那个盘子
        hanoi(n - 1, b, a, c)  # 将n-1个圆盘从b到a再到c


hanoi(3, 'A', 'B', 'C')

number = 0


def hanoi_number(n):
    if n > 0:
        hanoi_number(n - 1)
        global number
        number = number + 1
        hanoi_number(n - 1)
    return number


numbers = hanoi_number(3)
print("汉诺塔移动次数为:", numbers)
