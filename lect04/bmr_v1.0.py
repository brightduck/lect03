#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    作者：黄伟峰
    功能：BMR计算器
    版本：1.0
    日期：01/22/2018
"""

def main():
    """
        主函数
    """
    # 性别
    gender = '男'

    # 体重
    weight = 70

    # 身高
    height = 175

    # 年龄
    age = 25

    if gender == '男':
        bmr = 13.7 * weight + 5.0 * weight - 6.8 * age + 66
    elif gender == '女':
        bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
    else:
        bmr = -1


if __name__ == '__main__':
    main()