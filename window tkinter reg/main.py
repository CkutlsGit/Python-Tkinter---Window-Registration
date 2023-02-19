#Импорт библиотек 
import tkinter as Tk
import sys

#Создание окна и его названия
root =  Tk.Tk()
root.title("Login Window")


#Функция Account - Где изображается имя пользователя и пароль
def Account(widget):
    login_lbl.destroy()
    password_lbl.destroy()

    password_entry.delete(0, Tk.END)  
    login_entry.delete(0, Tk.END)
    password_entry.config(state="disabled")                           #<---- Отключение виджетов с прошлой регистрации и добавление новых виджетов
    login_entry.config(state="disabled")

    login_btn.destroy()

    login_user = Tk.Label(text=f"Your Login : {login}")
    login_user.grid(column=0, row=0)
    password_user = Tk.Label(text=f"Your Password: {password}")  # <------- Создание новых виджетов
    password_user.grid(column=0, row=1)

    warn_pas = Tk.Label(text="Никому не говорите cвой пароль")
    warn_pas.grid(column=1, row=1)
    warn_log = Tk.Label(text="Никому не сообщайте свой Логин кроме как Администрации!") 
    warn_log.grid(column=1, row=0)

    exit_button = Tk.Button(text="Exit", command=exit)
    exit_button.grid(column=2, row=2)

    print("Вы вошли в свой аккаунт!")

#Функция выхода из кода при нажатии на кнопку
def exit():
    print("Успешный выход")
    sys.exit()

def check_empty(entry):
    if not entry.strip():  #<-------- Проверка имеет ли поле ввода какие то данные, после чего эту проверку импортируем в функцию Login
        return True
    else:
        return False

login_lbl = Tk.Label(text="Login")
login_lbl.grid(column=0, row=0)
login_entry = Tk.Entry()
login_entry.grid(column=1, row=0)
#                                         Создание виджетов для регистрации
password_lbl = Tk.Label(text="Password")
password_lbl.grid(column=0, row=1)
password_entry = Tk.Entry(show="*")
password_entry.grid(column=1, row=1)

#Функция регистрации
def Login():
    global login, password
    login = login_entry.get()
    password = password_entry.get()
    if check_empty(login_entry.get()): #Импортированная проверка , имеет ли данные или нет
        print("To get started, enter the data!")
    else:
        if check_empty(password_entry.get()):
            print("To get started, enter the data!")
        else:
            print(f"User {login} successfully logged in")
            login_btn.bind('<Button-1>', Account) # Сделан переход , при нажатии кнопки - осуществляется переход в другую функцию.

#Создание кнопки Login
login_btn = Tk.Button(text="Login", command=Login)
login_btn.grid(column=1, row=2) 


#Важная строчка, позволяет работать всему процессу что происходит на экране.
root.mainloop()