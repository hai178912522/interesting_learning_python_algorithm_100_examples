# -*- coding: utf-8 -*-
# @Time : 2022/1/11 17:56
# @Author : ZZZZZHHHHH
# @FileName: 001_抓交通肇事犯.py
# @Software: PyCharm
if __name__ == '__main__':
    # i 代表前两位车牌号数字，j代表后两位车牌号的数字，k代表车牌
    # 穷举前两位和后两位车牌数字。
    for i in range(10):
        for j in range(10):
            # 判断i和j是否相等。
            if i != j:
                # 组成4位车牌号码
                k = 1000 * i + 100 * i + 10 * j + j
                for temp in range(31, 100):
                    if temp * temp == k:
                        print('车牌号为：', k)
