#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    作者：黄伟峰
    功能：BMR计算器
    版本：3.0
    日期：01/27/2018
    3.0 增加功能：用户可以在一行输入所有信息，带单位的信息输出
    4.0 增加功能：处理异常操作
"""

def main():
    """
        主函数
    """
    y_or_n = input('是否退出程序(y/n)?')
    while y_or_n != 'y':
        # # 性别
        # gender = input('性别：')
        #
        # # 体重
        # weight = float(input('体重(kg)：'))
        #
        # # 身高
        # height = float(input('身高（cm）:'))
        #
        # # 年龄
        # age = eval(input('年龄：'))
        print('请输入以下信息，用空格分割')
        input_str = input('性别 体重(kg) 身高(cm) 年龄：')
        str_list = input_str.split(' ')
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if gender == '男':
            bmr = 13.7 * weight + 5.0 * weight - 6.8 * age + 66
        elif gender == '女':
            bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
        else:
            bmr = -1

        if bmr != -1:
            print('您的性别；{}，体重{}公斤，身高：{}厘米，年龄：{}岁'.format(gender, weight, height, age))
            print('您的基础代谢率:{}（大卡）：'.format(bmr))
        else:
            print('暂不支持该性别')
        y_or_n = input('是否退出程序(y/n)?')

if __name__ == '__main__':
    main()