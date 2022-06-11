from tkinter import *

class my_calculator:
    def __init__(self,root):
        self.root=root
        self.root.title("CALCULATOR")
        self.expression=''
        self.txtinput=StringVar()

        ent_display=Entry(self.root,bd=7,bg='light blue',textvariable=self.txtinput,justify=RIGHT,font=(25))

        btn9 = Button(self.root,text='9',padx=20,pady=20,bg='yellow',command=lambda :self.btn_click(9))
        btn8 = Button(self.root, text='8',padx=20,pady=20,bg='yellow',command=lambda :self.btn_click(8))
        btn7 = Button(self.root, text='7',padx=20,pady=20,bg='yellow',command=lambda :self.btn_click(7))
        btn6 = Button(self.root, text='6',padx=20,pady=20,bg='yellow',command=lambda :self.btn_click(6))
        btn5 = Button(self.root, text='5',padx=20,pady=20,bg='yellow',command=lambda :self.btn_click(5))
        btn4 = Button(self.root, text='4',padx=20,pady=20,bg='yellow',command=lambda :self.btn_click(4))
        btn3 = Button(self.root, text='3',padx=20,pady=20,bg='yellow',command=lambda :self.btn_click(3))
        btn2 = Button(self.root, text='2',padx=20,pady=20,bg='yellow',command=lambda :self.btn_click(2))
        btn1 = Button(self.root, text='1',padx=20,pady=20,bg='yellow',command=lambda :self.btn_click(1))
        btn0 = Button(self.root, text='0',padx=20,pady=20,bg='yellow',command=lambda :self.btn_click(0))

        btndive= Button(self.root, text='/',padx=20,pady=20,bg='green',command=lambda :self.btn_click('/'))
        btnequal = Button(self.root, text='=',padx=20,pady=20,bg='black',fg='white',command=lambda :self.btn_equal())
        btnAC= Button(self.root, text='AC',padx=20,pady=20, bg='Red',command=lambda :self.btn_clr())
        btnsub = Button(self.root, text='-', bg='green',padx=20,pady=20,command=lambda :self.btn_click('-'))
        btnmulti = Button(self.root, text='*',padx=20,pady=20,bg='green',command=lambda :self.btn_click('*'))
        btnADD = Button(self.root, text='+',padx=20,pady=20,bg='green',command=lambda :self.btn_click('+'))
        
        ent_display.grid(row=0,columnspan=50)
        
        btn9.grid(row=1,column=0,padx=10,pady=10)
        btn8.grid(row=1,column=1, padx=10, pady=10)
        btn7.grid(row=1,column=2, padx=10, pady=10)
        btn6.grid(row=2,column=0, padx=10, pady=10)
        btn5.grid(row=2,column=1, padx=10, pady=10)
        btn4.grid(row=2,column=2, padx=10, pady=10)
        btn3.grid(row=3,column=0, padx=10, pady=10)
        btn2.grid(row=3,column=1, padx=10, pady=10)
        btn1.grid(row=3,column=2, padx=10, pady=10)
        btn0.grid(row=4,column=1, padx=10, pady=10)

        btndive.grid(row=4, column=2, padx=10, pady=10)
        btnequal.grid(row=4, column=3, padx=10, pady=10)
        btnAC.grid(row=4,column=0, padx=10, pady=10)
        btnsub.grid(row=2,column=3, padx=10, pady=10)
        btnmulti.grid(row=3,column=3, padx=10, pady=10)
        btnADD.grid(row=1,column=3, padx=10, pady=10)


    def btn_click(self,number):
        self.expression=self.expression+str(number)
        self.txtinput.set(self.expression)

    def btn_equal(self):
        cal=str(eval(self.expression))
        self.txtinput.set(cal)
        self.expression=''

    def btn_clr(self):
        self.txtinput.set('')
        self.expression=''



tk=Tk()
my_calculator(tk)
mainloop()