
import math as m

from tkinter import *
import tkinter as tk




LARGE_FONT_STYLE=("Arial", 40,"bold")
SMALL_FONT_STYLE=("Arial",16)
DIGITS_FONT_STYLE=("Arial",24,"bold")
DEFAULT_FONT_STYLE = ("Arial", 26)
DEFAULT_FONT_STYLE2 = ("Arial", 17,'bold')
OFF_WHITE = "#F0F8FF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
GRAY="#D3D3D3"
class calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("400x650+600+100")
        self.window.title("Calculator")
        self.window.minsize(400, 650)
        
       
        
        self.total_expression=""
        self.current_expression=""
        
        self.display_frame = self.create_display_frame()
        self.small_label, self.large_label = self.create_display_labels()
        
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        
        
        self.buttons_frame=self.create_buttons_frame()
        
        self.buttons_frame.pack()
        
        
        
        
        for i in range(1,5):
            
            self.buttons_frame.rowconfigure(i,weight=1)
            self.buttons_frame.columnconfigure(i,weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_equals_button()
        self.create_clear_button()
        self.bind_keys()
        menubar=Menu(self.window,font=("",100))
        mode=Menu(menubar,font=("",10),tearoff=0) 
        mode.add_checkbutton(label="Scientific",command=self.sc_click)
        menubar.add_cascade(label="◧",menu=mode)
       
        
        
        
        self.window.config(menu=menubar)
        self.normalcalc=True
    
    def sc_click(self):
        
        if self.normalcalc:
            self.window.geometry("650x650")
            self.window.minsize(650, 650)
            self.buttons2_frame=self.create_sbuttons_frame()
            self.buttons_frame.pack(side="right",expand=True,fill='both')
            self.buttons2_frame.pack(side="left",expand=True, fill='both')
            for i in range(1,7):
            
                self.buttons2_frame.rowconfigure(i,weight=1)
            for i in range(1,4):  
                self.buttons2_frame.columnconfigure(i,weight=1)
            self.create_sci_buttons()
            self.normalcalc=False

            
        else:
            self.window.geometry("400x650")
            self.window.minsize(400, 650)
            self.normalcalc=True
            self.buttons_frame.pack(side="top",expand=True, fill='both')
            self.buttons2_frame.destroy()
            
    def create_display_labels(self):
        small_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        small_label.pack(expand=True, fill='both')

        large_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        large_label.pack(expand=True, fill='both')

        return small_label, large_label

        
    def create_display_frame(self):
        frame = tk.Frame(self.window, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
            frame1=tk.Frame(self.window,height=300,bg='white')
            frame1.pack(expand=True, fill= "both")
            return frame1
    def create_sbuttons_frame(self):
            frame2=tk.Frame(self.window,height=300,bg="white")
            frame2.pack(expand=True, fill= "both")
            
            return frame2
    def create_sci_buttons(self):
        
        sci_button1=tk.Button(self.buttons2_frame,text='sin',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc("sin0"))
        sci_button1.grid(row=1,column=1,sticky=tk.NSEW)
        sci_button1.bind("<Enter>", func=lambda e: sci_button1.config(background=OFF_WHITE))
        sci_button1.bind("<Leave>", func=lambda e: sci_button1.config(background=LIGHT_BLUE))

        sci_button2=tk.Button(self.buttons2_frame,text='cos',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('cos0'))
        sci_button2.grid(row=1,column=2,sticky=tk.NSEW)
        sci_button2.bind("<Enter>", func=lambda e: sci_button2.config(background=OFF_WHITE))
        sci_button2.bind("<Leave>", func=lambda e: sci_button2.config(background=LIGHT_BLUE))

        sci_button3=tk.Button(self.buttons2_frame,text='tan',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('tan0'))
        sci_button3.grid(row=1,column=3,sticky=tk.NSEW)
        sci_button3.bind("<Enter>", func=lambda e: sci_button3.config(background=OFF_WHITE))
        sci_button3.bind("<Leave>", func=lambda e: sci_button3.config(background=LIGHT_BLUE))
        
        sci_button4=tk.Button(self.buttons2_frame,text='x!',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('x!'))
        sci_button4.grid(row=1,column=4,sticky=tk.NSEW)
        sci_button4.bind("<Enter>", func=lambda e: sci_button4.config(background=OFF_WHITE))
        sci_button4.bind("<Leave>", func=lambda e: sci_button4.config(background=LIGHT_BLUE))

        sci_button5=tk.Button(self.buttons2_frame,text='sin\u207b\u00b9',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('sin-1'))
        sci_button5.grid(row=2,column=1,sticky=tk.NSEW)
        sci_button5.bind("<Enter>", func=lambda e: sci_button5.config(background=OFF_WHITE))
        sci_button5.bind("<Leave>", func=lambda e: sci_button5.config(background=LIGHT_BLUE))

        sci_button6=tk.Button(self.buttons2_frame,text='cos\u207b\u00b9',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('cos-1'))
        sci_button6.grid(row=2,column=2,sticky=tk.NSEW)
        sci_button6.bind("<Enter>", func=lambda e: sci_button6.config(background=OFF_WHITE))
        sci_button6.bind("<Leave>", func=lambda e: sci_button6.config(background=LIGHT_BLUE))

        sci_button7=tk.Button(self.buttons2_frame,text='tan\u207b\u00b9',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('tan-1'))
        sci_button7.grid(row=2,column=3,sticky=tk.NSEW)
        sci_button7.bind("<Enter>", func=lambda e: sci_button7.config(background=OFF_WHITE))
        sci_button7.bind("<Leave>", func=lambda e: sci_button7.config(background=LIGHT_BLUE))
        
        sci_button8=tk.Button(self.buttons2_frame,text='x\u207f',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.add_to_expression('**'))
        sci_button8.grid(row=2,column=4,sticky=tk.NSEW)
        sci_button8.bind("<Enter>", func=lambda e: sci_button8.config(background=OFF_WHITE))
        sci_button8.bind("<Leave>", func=lambda e: sci_button8.config(background=LIGHT_BLUE))

        sci_button9=tk.Button(self.buttons2_frame,text='ln',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('ln'))
        sci_button9.grid(row=3,column=1,sticky=tk.NSEW)
        sci_button9.bind("<Enter>", func=lambda e: sci_button9.config(background=OFF_WHITE))
        sci_button9.bind("<Leave>", func=lambda e: sci_button9.config(background=LIGHT_BLUE))

        sci_button10=tk.Button(self.buttons2_frame,text='log',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('log'))
        sci_button10.grid(row=3,column=2,sticky=tk.NSEW)
        sci_button10.bind("<Enter>", func=lambda e: sci_button10.config(background=OFF_WHITE))
        sci_button10.bind("<Leave>", func=lambda e: sci_button10.config(background=LIGHT_BLUE))

        sci_button11=tk.Button(self.buttons2_frame,text='%',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.add_to_expression('%'))
        sci_button11.grid(row=3,column=3,sticky=tk.NSEW)
        sci_button11.bind("<Enter>", func=lambda e: sci_button11.config(background=OFF_WHITE))
        sci_button11.bind("<Leave>", func=lambda e: sci_button11.config(background=LIGHT_BLUE))
        

        sci_button12=tk.Button(self.buttons2_frame,text='x\u207b\u00b9',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('x-1'))
        sci_button12.grid(row=3,column=4,sticky=tk.NSEW)
        sci_button12.bind("<Enter>", func=lambda e: sci_button12.config(background=OFF_WHITE))
        sci_button12.bind("<Leave>", func=lambda e: sci_button12.config(background=LIGHT_BLUE))

        sci_button13=tk.Button(self.buttons2_frame,text='e',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.add_to_expression('2.178'))
        sci_button13.grid(row=4,column=1,sticky=tk.NSEW)
        sci_button13.bind("<Enter>", func=lambda e: sci_button13.config(background=OFF_WHITE))
        sci_button13.bind("<Leave>", func=lambda e: sci_button13.config(background=LIGHT_BLUE))

        sci_button14=tk.Button(self.buttons2_frame,text='e\u207f',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.add_to_expression('2.178**'))
        sci_button14.grid(row=4,column=2,sticky=tk.NSEW)
        sci_button14.bind("<Enter>", func=lambda e: sci_button14.config(background=OFF_WHITE))
        sci_button14.bind("<Leave>", func=lambda e: sci_button14.config(background=LIGHT_BLUE))

        sci_button15=tk.Button(self.buttons2_frame,text='\u03c0',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.add_to_expression('3.1415'))
        sci_button15.grid(row=4,column=3,sticky=tk.NSEW)
        sci_button15.bind("<Enter>", func=lambda e: sci_button15.config(background=OFF_WHITE))
        sci_button15.bind("<Leave>", func=lambda e: sci_button15.config(background=LIGHT_BLUE))
        

        sci_button16=tk.Button(self.buttons2_frame,text='\u221bx',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('x^1/3'))
        sci_button16.grid(row=4,column=4,sticky=tk.NSEW)
        sci_button16.bind("<Enter>", func=lambda e: sci_button16.config(background=OFF_WHITE))
        sci_button16.bind("<Leave>", func=lambda e: sci_button16.config(background=LIGHT_BLUE))
        
        sci_button17=tk.Button(self.buttons2_frame,text='\u230ax\u230b',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('xg'))
        sci_button17.grid(row=5,column=1,sticky=tk.NSEW)
        sci_button17.bind("<Enter>", func=lambda e: sci_button17.config(background=OFF_WHITE))
        sci_button17.bind("<Leave>", func=lambda e: sci_button17.config(background=LIGHT_BLUE))

        sci_button18=tk.Button(self.buttons2_frame,text='\u2308x\u2309',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('xs'))
        sci_button18.grid(row=5,column=2,sticky=tk.NSEW)
        sci_button18.bind("<Enter>", func=lambda e: sci_button18.config(background=OFF_WHITE))
        sci_button18.bind("<Leave>", func=lambda e: sci_button18.config(background=LIGHT_BLUE))

        sci_button19=tk.Button(self.buttons2_frame,text='+/-',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('+/-'))
        sci_button19.grid(row=5,column=3,sticky=tk.NSEW)
        sci_button19.bind("<Enter>", func=lambda e: sci_button19.config(background=OFF_WHITE))
        sci_button19.bind("<Leave>", func=lambda e: sci_button19.config(background=LIGHT_BLUE))
        

        sci_button20=tk.Button(self.buttons2_frame,text='x10\u207f',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.add_to_expression('*10**'))
        sci_button20.grid(row=5,column=4,sticky=tk.NSEW)
        sci_button20.bind("<Enter>", func=lambda e: sci_button20.config(background=OFF_WHITE))
        sci_button20.bind("<Leave>", func=lambda e: sci_button20.config(background=LIGHT_BLUE))

        sci_button21=tk.Button(self.buttons2_frame,text='(',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.add_to_expression('('))
        sci_button21.grid(row=6,column=1,sticky=tk.NSEW)
        sci_button21.bind("<Enter>", func=lambda e: sci_button21.config(background=OFF_WHITE))
        sci_button21.bind("<Leave>", func=lambda e: sci_button21.config(background=LIGHT_BLUE))

        sci_button22=tk.Button(self.buttons2_frame,text=')',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.add_to_expression(')'))
        sci_button22.grid(row=6,column=2,sticky=tk.NSEW)
        sci_button22.bind("<Enter>", func=lambda e: sci_button22.config(background=OFF_WHITE))
        sci_button22.bind("<Leave>", func=lambda e: sci_button22.config(background=LIGHT_BLUE))

        sci_button23=tk.Button(self.buttons2_frame,text='DEG',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('DEG'))
        sci_button23.grid(row=6,column=3,sticky=tk.NSEW)
        sci_button23.bind("<Enter>", func=lambda e: sci_button23.config(background=OFF_WHITE))
        sci_button23.bind("<Leave>", func=lambda e: sci_button23.config(background=LIGHT_BLUE))
        

        sci_button24=tk.Button(self.buttons2_frame,text='RAD',bg=LIGHT_BLUE,fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE2,borderwidth=0,command=lambda:self.calculate_sc('RAD'))
        sci_button24.grid(row=6,column=4,sticky=tk.NSEW)
        sci_button24.bind("<Enter>", func=lambda e: sci_button24.config(background=OFF_WHITE))
        sci_button24.bind("<Leave>", func=lambda e: sci_button24.config(background=LIGHT_BLUE))
       
    def calculate_sc(self,event):
        
        text=str(event)
        ex=self.current_expression
        answer=''
        
        if text=="sin0":
            answer=str(m.sin(m.radians(float(ex))))
        
        elif text=="cos0":
            answer=str(m.cos(m.radians(float(ex))))
        
        elif text=="tan0":
            answer=str(m.tan(m.radians(float(ex))))
        elif text=="x!":
            answer=str(m.factorial(int(ex)))
        elif text=="sin-1":
            answer=str(m.degrees(m.asin(float(ex))))
        
        elif text=="cos-1":
            answer=str(m.degrees(m.acos(float(ex))))
        elif text=="tan-1":
            answer=str(m.degrees(m.atan(float(ex))))
        
        
        elif text=="ln":
            answer=str(m.log(float(ex)))
        elif text=="log":
            answer=str(m.log(float(ex),10))
        
        elif text=="x-1":
            answer=str(float(1/(float(ex))))
        elif text=="x^1/3":
            answer=str(eval(str((float(ex))**float(1/3))))
        elif text=="xs":
            answer=str(m.ceil(float(ex)))
        elif text=="xg":
            answer=str(m.floor(float(ex)))
        elif text=="+/-":
            if float(ex)>0:
                answer='-'+str(ex)
            else:
                answer=str(abs(float(ex)))
        
        elif text=="RAD":
            answer=str(m.radians(float(ex)))
        
        elif text=="DEG":
            answer=str(m.degrees(float(ex)))
        
        
        
        #self.large_label["text"]=""    
        self.large_label["text"]=answer
        self.current_expression=answer
     
        

        

    
        
    def create_digit_buttons(self):
        button7=tk.Button(self.buttons_frame,text='7',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda:self.add_to_expression(7))
        button7.grid(row=1,column=1,sticky=tk.NSEW)
        button7.bind("<Enter>", func=lambda e: button7.config(background=GRAY))
        button7.bind("<Leave>", func=lambda e: button7.config(background=WHITE))

        button8=tk.Button(self.buttons_frame,text='8',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda:self.add_to_expression(8))
        button8.grid(row=1,column=2,sticky=tk.NSEW)
        button8.bind("<Enter>", func=lambda e: button8.config(background=GRAY))
        button8.bind("<Leave>", func=lambda e: button8.config(background=WHITE))

        button9=tk.Button(self.buttons_frame,text='9',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda:self.add_to_expression(9))
        button9.grid(row=1,column=3,sticky=tk.NSEW)
        button9.bind("<Enter>", func=lambda e: button9.config(background=GRAY))
        button9.bind("<Leave>", func=lambda e: button9.config(background=WHITE))

        button4=tk.Button(self.buttons_frame,text='4',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda:self.add_to_expression(4))
        button4.grid(row=2,column=1,sticky=tk.NSEW)
        button4.bind("<Enter>", func=lambda e: button4.config(background=GRAY))
        button4.bind("<Leave>", func=lambda e: button4.config(background=WHITE))

        button5=tk.Button(self.buttons_frame,text='5',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda:self.add_to_expression(5))
        button5.grid(row=2,column=2,sticky=tk.NSEW)
        button5.bind("<Enter>", func=lambda e: button5.config(background=GRAY))
        button5.bind("<Leave>", func=lambda e: button5.config(background=WHITE))

        button6=tk.Button(self.buttons_frame,text='6',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda:self.add_to_expression(6))
        button6.grid(row=2,column=3,sticky=tk.NSEW)
        button6.bind("<Enter>", func=lambda e: button6.config(background=GRAY))
        button6.bind("<Leave>", func=lambda e: button6.config(background=WHITE))

        button1=tk.Button(self.buttons_frame,text='1',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda:self.add_to_expression(1))
        button1.grid(row=3,column=1,sticky=tk.NSEW)
        button1.bind("<Enter>", func=lambda e: button1.config(background=GRAY))
        button1.bind("<Leave>", func=lambda e: button1.config(background=WHITE))

        button2=tk.Button(self.buttons_frame,text='2',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda:self.add_to_expression(2))
        button2.grid(row=3,column=2,sticky=tk.NSEW)
        button2.bind("<Enter>", func=lambda e: button2.config(background=GRAY))
        button2.bind("<Leave>", func=lambda e: button2.config(background=WHITE))

        button3=tk.Button(self.buttons_frame,text='3',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda:self.add_to_expression(3))
        button3.grid(row=3,column=3,sticky=tk.NSEW)
        button3.bind("<Enter>", func=lambda e: button3.config(background=GRAY))
        button3.bind("<Leave>", func=lambda e: button3.config(background=WHITE))

        button_dot=tk.Button(self.buttons_frame,text='•',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda:self.add_to_expression("."))
        button_dot.grid(row=4,column=1,sticky=tk.NSEW)
        button_dot.bind("<Enter>", func=lambda e: button_dot.config(background=GRAY))
        button_dot.bind("<Leave>", func=lambda e: button_dot.config(background=WHITE))

        button0=tk.Button(self.buttons_frame,text='0',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda:self.add_to_expression(0))
        button0.grid(row=4,column=2,sticky=tk.NSEW)
        button0.bind("<Enter>", func=lambda e: button0.config(background=GRAY))
        button0.bind("<Leave>", func=lambda e: button0.config(background=WHITE))

        button_back=tk.Button(self.buttons_frame,text='«',bg=WHITE,fg=LABEL_COLOR,
                    font=DIGITS_FONT_STYLE,borderwidth=0,command=self.backspace_to_expression)
        button_back.grid(row=4,column=3,sticky=tk.NSEW)
        button_back.bind("<Enter>", func=lambda e: button_back.config(background=GRAY))
        button_back.bind("<Leave>", func=lambda e: button_back.config(background=WHITE))
    def create_operator_buttons(self):
        self.button_divide = tk.Button(self.buttons_frame, text="\u00F7", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0,command=lambda : self.append_operator("/"))
        self.button_divide.grid(row=0, column=4, sticky=tk.NSEW)
        self.button_divide.bind("<Enter>", func=lambda e: self.button_divide.config(background=GRAY))
        self.button_divide.bind("<Leave>", func=lambda e: self.button_divide.config(background=OFF_WHITE))
    
        self.button_multi = tk.Button(self.buttons_frame, text="\u00D7", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0,command=lambda : self.append_operator("*"))
        self.button_multi.grid(row=1, column=4, sticky=tk.NSEW)
        self.button_multi.bind("<Enter>", func=lambda e: self.button_multi.config(background=GRAY))
        self.button_multi.bind("<Leave>", func=lambda e: self.button_multi.config(background=OFF_WHITE))

        self.button_sub = tk.Button(self.buttons_frame, text="-", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0,command=lambda : self.append_operator("-"))
        self.button_sub.grid(row=2, column=4, sticky=tk.NSEW)
        self.button_sub.bind("<Enter>", func=lambda e: self.button_sub.config(background=GRAY))
        self.button_sub.bind("<Leave>", func=lambda e: self.button_sub.config(background=OFF_WHITE))

        self.button_add = tk.Button(self.buttons_frame, text="+", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0,command=lambda : self.append_operator("+"))
        self.button_add.grid(row=3, column=4, sticky=tk.NSEW)
        self.button_add.bind("<Enter>", func=lambda e: self.button_add.config(background=GRAY))
        self.button_add.bind("<Leave>", func=lambda e: self.button_add.config(background=OFF_WHITE))
            
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0,command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)
        button.bind("<Enter>", func=lambda e: button.config(background=GRAY))
        button.bind("<Leave>", func=lambda e: button.config(background=OFF_WHITE))
    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0,command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)
        button.bind("<Enter>", func=lambda e: button.config(background=GRAY))
        button.bind("<Leave>", func=lambda e: button.config(background=OFF_WHITE))
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0,command=self.evaluate)
        button.grid(row=4, column=4, sticky=tk.NSEW)
        button.bind("<Enter>", func=lambda e: button.config(background=GRAY))
        button.bind("<Leave>", func=lambda e: button.config(background=LIGHT_BLUE))
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0,command=self.clear)
        
        button.grid(row=0, column=1, sticky=tk.NSEW)
        button.bind("<Enter>", func=lambda e: button.config(background=GRAY))
        button.bind("<Leave>", func=lambda e: button.config(background=OFF_WHITE))
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_large_label()
        self.update_small_label()
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        self.window.bind("<BackSpace>", lambda event: self.backspace_to_expression())
        self.window.bind("<.>", lambda event, digit='.': self.add_to_expression(digit))
        for i in range(0,10):
            self.window.bind(str(i), lambda event, digit=i: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))
    def backspace_to_expression(self):
        self.current_expression = self.current_expression[0:-1:1]
        self.update_large_label()

    def add_to_expression(self, value):
        
        self.current_expression += str(value)
        self.update_small_label()
        self.update_large_label()
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_large_label()
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_large_label()
   


    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_small_label()
        self.update_large_label()
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_small_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            
            self.update_large_label()
    def update_small_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f" {symbol} ")
        self.small_label.config(text=expression)

    def update_large_label(self):
        self.large_label.config(text=self.current_expression[::])
        
        

    
    def run(self):
            self.window.mainloop()


if __name__ == "__main__":
    calc=calculator()
    calc.run()
