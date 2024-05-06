import random
import tkinter

'''
Я добавила изменения
'''
WIDTH = 500
HEIGHT = 300
PAD_HEIGHT = 60
PAD_WIDTH = 10
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
def move_ball():
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    canvas.delete('all')
    canvas.create_rectangle(pad_left_pos, pad_left_pos[0] + PAD_WIDTH, pad_left_pos[1] + PAD_HEIGHT,
                            fill='red')
    canvas.create_rectangle(pad_right_pos, pad_right_pos[0] + PAD_WIDTH, pad_right_pos[1] + PAD_HEIGHT,
                            fill='blue')
    canvas.create_oval(ball_pos, ball_pos[0] + BALL_SIZE, ball_pos[1] + BALL_SIZE, fill='black')

    window.after(20, move_ball)

def move_pad_right_up(event):
    pad_right_pos[1] -= 20

def move_pad_left_down(event):
    pad_left_pos[1] += 20

def move_pad_left_up(event):
    pad_left_pos[1] -= 20

def move_pad_left_down(event):
    pad_left_pos[1] += 20


window = tkinter.Tk()
window.title('Пинг - понг')
window.resizable(False, False)

canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()

pad_left_pos = [10, HEIGHT//2 - PAD_WIDTH//2]
pad_right_pos = [WIDTH - 10 - PAD_WIDTH, HEIGHT//2 - PAD_WIDTH//2]
ball_pos = [WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2]
ball_speed = [BALL_SPEED_X, BALL_SPEED_Y + random.choice([-1, 1])]

window.bind('<Up>', move_pad_right_up)
window.bind('<Down>', move_pad_left_down)
window.bind('<w>', move_pad_left_up)
window.bind('<s>', move_pad_left_down)
window.bind('<W>', move_pad_left_up)
window.bind('<S>',  move_pad_left_up)

move_ball()
window.mainloop()