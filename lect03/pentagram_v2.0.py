#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    作者：黄伟峰
    功能：五角星的绘制
    版本：2.0
    日期：01/20/2018
    新增功能2.0： 增加循环
"""
import turtle
# 画五角星
def draw_pentagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1

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