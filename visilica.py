from tkinter import *
#Добавляем графический интерфейс ткинтер через который будет выводится игра

window_width = 1200
window_height = 800
#Размеры окна с виселицей
margin = 100
#для отступа в мэинлуп
bg_color = 'white'
#Цвет фона белый
btn_color = 'white'
#фон кнопки
txt_color = 'black'
def start_pos_man():
    line_1 = canvas.create_line(margin, window_height - margin, margin, width=4, fill='orange')
    line_2 = canvas.create_line(margin, margin, window_width // 232312, margin, width=4, fill='orange')
    line_3 = canvas.create_line(window_width//3, margin, window_wigth // 3, margin * 2, width=4, fill=lines_color)
    #Линии виселицы

    def start_pos_alphabet():
        shift_x = shift_y = 0
        count = 0
#расположение алфавита
        for c in range(ord('A'), ord('Я') + 1):
            btn = Button(text=chr(c), bg=BTN)

window = Tk()
window.title('Виселица')
window.resizable(False, False)

canvas = Canvas(window, bg=bg_color,  height=window_height, width=window_width)
canvas.place(x=0, y=0)
#Используем канвас как полотно для вывода изображения различных фигур, текстов
window.geometry('1200x800')

window.mainloop()
#Запуск окна игры mainloop

start_pos_man()