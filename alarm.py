import datetime
import tkinter as tk
import pygame

class Alar_X_Clock:
    def __init__(self):
        #Подготовка
        self.window = tk.Tk()
        self.window.title("Будильник")
        self.window.geometry("350x500+850+300")
        self.window.resizable(False,False)
        self.icon = tk.PhotoImage(file = r"C:\Users\Melni\Desktop\alarm\alarm.png")
        self.window.iconphoto(False,self.icon)

        #Часы
        self.Frame = tk.Frame(self.window, bg="#FFDAB9", bd=10, relief="raised")
        self.Frame.pack(fill = "both", expand=True)
        self.timelab = tk.Label(self.window, text="",background = "#FFFFFF",borderwidth= 5, relief = "ridge", font=("Arial Bold", 40))
        self.timelab.place(x = 105, y = 30)

        #Хеадер
        self.lbl = tk.Label(self.window, text = "Режимы работы:", bg="#FFDAB9",foreground="black", font = ("Arial Bold", 14))
        self.lbl.place(x = 20, y = 120)
        
        #Радио
        self.var = tk.IntVar()
        #self.var.set(0)
        self.b1 = tk.Radiobutton(self.window, text = "Режим установки времени", bg="#FFDAB9", variable=self.var, value=1, command=self.pickradio)
        self.b1.place(x = 20, y = 150)
        self.b2 = tk.Radiobutton(self.window, text = "Режим установки времени срабатывания",bg="#FFDAB9", variable=self.var,value=2,command=self.pickradio)
        self.b2.place(x = 20, y = 170)
        self.b3 = tk.Radiobutton(self.window, text = "Сброс",bg="#FFDAB9", variable=self.var,value=3,command=self.pickradio)
        self.b3.place(x = 20, y = 190)   

        #Часики и ползунки
        self.timelab1 = tk.Label(self.window, text="00:00",background = "#FFFFFF",borderwidth= 5, relief = "ridge", font=("Arial Bold", 25))
        self.timelab1.place(x = 23, y = 220)
        self.timelab2 = tk.Label(self.window, text="00:00",background = "#FFFFFF",borderwidth= 5, relief = "ridge", font=("Arial Bold", 25))
        self.timelab2.place(x = 123, y = 220)
        self.varsh = tk.IntVar()
        self.varsm = tk.IntVar()
        self.spinH = tk.Spinbox(self.window,from_ = 0.0, to = 23.0,textvariable = self.varsh,state="disabled",wrap=True, command=self.swaptime)
        self.spinM = tk.Spinbox(self.window,from_ = 0.0, to = 59.0, textvariable= self.varsm,state = "disabled",wrap=True, command=self.swaptime)
        self.spinH.place(x = 240, y = 220,width=60)
        self.spinM.place(x = 240, y = 250,width=60)

        #Кнопки
        self.lbl1 = tk.Label(self.window, text="Включение/Выключение",bg="#FFDAB9",foreground="black", font = ("Arial Bold", 14))
        self.lbl1.place(x = 20, y = 285)
        self.onoff = tk.Button(self.window, text="Вкл",font = ("Arial Bold", 10), command=self.butONOFF)
        self.onoff.place(x = 245, y = 285, width=50)

        #Подготовка радио
        pygame.init()
        self.sound = pygame.mixer.music.load(r"C:\Users\Melni\Desktop\alarm\rad.mp3")
        
        #Радио
        self.radio = tk.Button(self.window, text="Радио",font = ("Arial Bold", 14),command=self.radioplay)
        self.radio.place(x = 20, y = 350, width=100)
        

        #Таймер
        self.timer = tk.Button(self.window, text="Таймер", font = ("Arial Bold", 14),command=self.Timer1)
        self.timer.place(x = 225, y = 350, width=100)

        #Конечная часть

        self.curTime()
        
        self.window.mainloop() 

        #Функции


    def AlarmFinally(self):
        hours1, minutes1 = map(int, self.timelab1["text"].split(":"))
        hours2, minutes2 = map(int, self.timelab2["text"].split(":"))
        selected = self.var.get()
        if (hours1 < hours2) or (hours1 == hours2 and minutes1 < minutes2) and selected == 1:
            if minutes1 < 59:
                minutes1 += 1
            else:
                minutes1 = 0
                hours1 += 1
            self.timelab1["text"] = f"{hours1:02d}:{minutes1:02d}"
            self.window.after(60*1000, self.AlarmFinally)
        elif hours1 == hours2 and minutes1 == minutes2:
            pygame.mixer.music.play(-1) 
        

    def Timer1(self):
        # self.timelab2.config(text="00:30")
        self.MM = 30
        selected = self.var.get()
        if selected == 2:
            self.timelab2["text"] = f"00:{self.MM:02}"
        else:
            self.timelab2.config(text="00:00")
            pygame.mixer.music.stop()
        self.Timer2()

    def Timer2(self):
        pygame.mixer.music.play(-1)
        self.MM -= 1
        
        
        if self.MM > 0:
            self.window.after(60*1000, self.Timer2)
        else:
            pygame.mixer.music.stop()

    def radioplay(self):
        if self.radio and (self.onoff.config("text")[-1] == "Вкл"):
            pygame.mixer.music.play(-1)
        elif self.onoff.config("text")[-1] == "Выкл":
            pygame.mixer.music.stop()
        elif self.radio:
            pygame.mixer.music.stop()
            

    def butONOFF(self):
        if self.onoff.config("text")[-1] == "Вкл":
            self.onoff.config(text = "Выкл")
            self.AlarmFinally()
        else:
            self.onoff.config(text = "Вкл")
            pygame.mixer.music.stop()
        
    def curTime(self):
        cutt = datetime.datetime.now().strftime("%H:%M")
        self.timelab.config(text = cutt)
        self.window.after(1000,self.curTime)
    
    def swaptime(self):
        H = self.varsh.get()
        M = self.varsm.get()
        if H < 10:
             H1 = f"0{H}"
        else:
            H1 = H
        if M < 10:
            M1 = f"0{M}"
        else:
            M1 = M
        selected = self.var.get()
        if selected == 1:
            self.timelab1.config(text = f"{H1}:{M1}")
        elif selected == 2:
            self.timelab2.config(text = f"{H1}:{M1}")

    def pickradio(self):
        selected = self.var.get()
        if selected == 1:
            self.spinH.config(state = "normal")
            self.spinM.config(state = "normal")
            self.varsh.set(0)
            self.varsm.set(0)
        elif selected == 2:
            self.spinH.config(state = "normal")
            self.spinM.config(state = "normal")
            self.varsh.set(0)
            self.varsm.set(0)
        elif selected == 3:
            self.spinH.config(state = "disabled")
            self.spinM.config(state = "disabled")
            self.varsh.set(0)
            self.varsm.set(0)
            self.timelab1.config(text = "00:00")
            self.timelab2.config(text = "00:00")
        else:
            self.spinH.config(state = "disabled")
            self.spinM.config(state = "disabled")
            self.varsh.set(0)
            self.varsm.set(0)







Pusk = Alar_X_Clock()