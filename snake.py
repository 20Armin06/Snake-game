from codecs import xmlcharrefreplace_errors
from tkinter import *
from random import*

#ساخت دستور مورد نیاز
def create_food():
    global food
    if food:
        canvas.delete(food)
    x=randint(0,(Width//seg_size)-1)*seg_size
    y=randint(0,(Height//seg_size)-1)*seg_size
    food=canvas.create_oval(x,y,x+seg_size,y+seg_size,fill="red",outline="orange",width=2)
def move_snake():
    global snake,direction
    head_x,head_y=snake[0]
    #تغییر جهت مار
    if direction=="Left":
        head_x -= seg_size
    elif direction=="Right":
        head_x+=seg_size
    elif direction=="Up":
        head_y-=seg_size
    elif direction=="Down":
        head_y+=seg_size
    new_head=(head_x,head_y)
    #بررسی برخورد مار با دیوار یا خودش
    if check_colisoion(new_head):
        game_over()
        return
    snake.insert(0,new_head)
    food_cords=canvas.coords(food)
    if new_head==(food_cords[0],food_cords[1]):
        create_food()
    else:
        snake.pop()
    #رسم مار
    canvas.delete("snake")
    for i , segment in enumerate(snake):
        color="purple" if i==0 else "pink"
        shade_color="gray"
        #سایه مار
        canvas.create_oval(segment[0]+2,segment[1]+2,segment[0]+seg_size,segment[1]+seg_size,fill=shade_color,outline=shade_color,tag="snake")
        #رسم بدن مار
        canvas.create_oval(segment[0] , segment[1] , segment[0] + seg_size, segment[1] + seg_size,fill=shade_color, outline=shade_color, tag="snake")
    mar.after(100,move_snake)
def check_colisoion(new_head):
    x,y=new_head
    if x<0 or x>=Width or y<0 or y>=Height or new_head in snake[1:]:
        return True
    else:
        return False

def change_direction(event):
    global direction
    new_direction=event.keysym
    op={"Left":"Right","Right":"left","Up":"Down","Down":"up"}
    if new_direction in op and new_direction !=op[direction]:
        direction=new_direction


def game_over():
    canvas.create_text(Width//2,Height//2,text="باختی",fill="red",font=("Aldhabi",60,'bold'))


#ابعاد و متغیر ها
Width=500
Height=500
seg_size=20
food=None
snake=[(240,240),(220,240),(200,240)]
direction="Right"

mar=Tk()
mar.title("mar bazi")
#mar.iconbitmap("download.ico")
#ساخت بوم نقاشی
canvas=Canvas(mar,width=Width,height=Height,bg="green")
canvas.pack()
#اتصال کلید های داده شده به برنامه
canvas.bind_all("<KeyPress>",change_direction)
#شروع بازی
create_food()
move_snake()
mar.mainloop()