# 学习turtle的图形化编程
import turtle

turtle = turtle  #  避免报错,不可显示调用
turtle.showturtle()  # 显示箭头
turtle.write("test")  # 写字符串
turtle.forward(300)  # 前进300像素
turtle.width(10)  # 画线的宽度
turtle.color("blue")  # 画笔颜色改为蓝色
turtle.circle(50)  # 从当前点开始画圆,半径为50,注意当前点不是圆的原点,是圆周上的点
turtle.left(30)  # 箭头左转30度
turtle.penup()  # 抬起画笔,路径将不会显示
turtle.goto(120, 0)  # 去坐标(120,0),默认画布中间为0,0
turtle.pendown()  # 画笔落下,重新显示路径
