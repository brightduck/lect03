#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    作者：黄伟峰
    功能：利用递归函数，绘制分形树
    版本：3.0
    日期：01/20/2018
    新增功能2.0： 增加循环
    新增功能3.0： 递归函数 使用迭代函数绘制不同大小的函数
"""
import turtle
def draw_branch(branch_length):
    """
    绘制分形树函数
    """
    if branch_length > 5:
        # 绘制右侧的树枝
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)
        # 绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length - 15)
        # 返回之前的树枝
        turtle.right(20)
        turtle.backward(branch_length)

def main():
    """
        主函数
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.pencolor('brown')
    draw_branch(80)


if __name__ == '__main__':
    main()