''' Random Turtle p.86 - var. Dice '''

from turtle import *
import random

stop_flag = False # 実行停止フラグ

def clicked(x, y):
    ''' マウスがクリックされた時の関数
        引数x, y をとるようにしないといけないが使わない
        実行停止フラグを True にする '''

    global stop_flag
    stop_flag = True
    
    
# onscreenclick(clicked)
''' マウスがクリックされた時の動作 clicked に () を付けない '''

def draw_text(x, y):
    label = [i for i in range(2, 13)]
    
    for i in label:
        penup()
        goto(x, y)
        pendown()
        write(arg=i, move=False, align='center', font=('Sans', 12))
        x += 30
    
    
def draw_box(x, y):
    penup()
    goto(x, y)
    pendown()
    forward(20)
    left(90)
    forward(5)
    left(90)
    forward(20)
    left(90)
    forward(5)
    left(90)
    penup()
   
    
speed(0)  # 0:max, 1:min

# initial
point_y = -200
history = [0] * 11  # 履歴を保管するリスト
count = 120  # サイコロを振る回数を指定

draw_text(-147, -220)  # 左下の適当な位置

while count > 0:  # while not stop_flag:

    # サイコロの目   
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_sum = dice_1 + dice_2
    
    history[dice_sum - 2] += 5  # boxの高さ分
        
    point_x = (dice_sum - 2) * 30 -160
    
    draw_box(point_x, history[dice_sum -2] + point_y)
    
    count -= 1

done()
