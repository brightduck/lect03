#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    作者：黄伟峰
    功能：五角星的绘制
    版本：3.0
    日期：01/20/2018
    新增功能2.0： 增加循环
    新增功能3.0： 递归函数 使用迭代函数绘制不同大小的函数
"""
import turtle
# 画五角星
def draw_pentagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1

def draw_recursive_pentgram(size)
    """
        迭代绘制五角星
    """
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1
    # 五角星绘制完成，更新参数
    size += 10
    if size <= 100:
        draw_recursive_pentgram(size)


def main():
    """
        主函数
    """
    # 计数器
    size = 50
    while size <= 100:
        draw_pentagram(size)
        size = size + 10

    turtle.exitonclick()

if __name__ == '__main__':
    main()