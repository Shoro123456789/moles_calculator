import re
import customtkinter as ctk
from tkinter.font import Font
from tkinter import ttk
from tkinter import StringVar
from os import *
from time import *

const = 6.022*(10**23)
gas = 24


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        start_time = time()
        self.title("Element Calculator")
        self.geometry("250x150")
        self.calc = calculator(master=self)
        self.calc.pack()
        # self.load = loading(master=self)
        # self.load.pack()
        # if (time()-start_time) > 500:
        #     self.load.destroy()

        self.mainloop()

#class loading(ctk.CTkFrame):
#    def __init__(self, master):
#        ctk.CTkFrame.__init__(self, master)
#        self.label = ctk.CTkLabel(self, text="Loading...")
#        self.label.pack()
class calculator(ctk.CTkFrame): 
    def __init__(self,master):
        ctk.CTkFrame.__init__(self, master)
        bold_font = ctk.CTkFont(family="Helvetica", size=13, weight="bold")


        self.frame1= ctk.CTkFrame(master=self)
        self.frame1.pack()

        self.tabs = ctk.CTkTabview(master=self.frame1, height=80, anchor="w")
        self.tabs.pack()
        self.tabs.add("Calculation")
        self.tabs.add("info")

        self.elm_input = StringVar()
        self.calculate_input = ctk.CTkEntry(master=self.tabs.tab("Calculation"), width=220, font=bold_font, placeholder_text="Enter Element", textvariable=self.elm_input)

        self.calculate_input.pack()

        self.calculate_output_converted = ctk.CTkLabel(master=self.tabs.tab("Calculation"), text="")
        self.calculate_output = ctk.CTkLabel(master=self.tabs.tab("Calculation"), text="")
        self.calculate_button = ctk.CTkButton(master=self.tabs.tab("Calculation"), text="Calculate", command=self.calculate, width=15)
        self.calculate_button.pack()
        info_text = ctk.CTkLabel(master=self.tabs.tab("info"), text="this is a mole calculator so inputted elements are their mass numbers (example: H2 is actually gonna be percieved as 2 as hydrogens mass number is 1)" + "\n" + "\n" +  "Rules: firstly you should enter the elm.element, then press the calculate button." + "\n" + "\n" + "Example: H2, then press the calculate button." + "\n" + "\n" + "Secondly, you should have the elm.element's chemical symbol correctly(example: NaCl and not nacl)" + "\n" + "\n" + "Thirdly, if there is more than one moles of a compound then input it like this (example: 5*(H2O))" + "\n" + "\n" + "You can write the word -const- to multiply the mass number by avagadros constant/6.022*(10**23)")
        info_text.pack()
#        self.info = ctk.CTkButton(master=self.frame1, text="Info", command=self.info, width=15)
#        self.info.pack()
        history = ctk.CTkButton(master=self.frame1, text="History", command=self.history, width=15)
        #history.pack()

        self.calculate_output_converted.pack()
        self.calculate_output.pack()

    """
    This function calculates the output of the 
    checmical formula provided by the user.
    """
    def calculate(self):
        try:
            self.element = self.elm_input
            print("working")
            print(self.element)
            self.element = re.sub(r" ", r"", self.element.get())
            self.element = re.sub(r"(\d+(\.\d+)?)(g)", r"(\1*1)", self.element)
            self.element = re.sub(r"(\d+(\.\d+)?)(mg)", r"(\1*0.001)", self.element)
            self.element = re.sub(r"(\d+(\.\d+)?)(Kg)", r"(\1*1000)", self.element, flags=re.IGNORECASE)
            self.element = re.sub(r"(\d+(\.\d+)?)(Tonnes)", r"(\1*1000000)", self.element, flags=re.IGNORECASE)
            self.element = re.sub(r"(\d+(\.\d+)?)(dm3)", r"(\1*1)", self.element)
            self.element = re.sub(r"(\d+(\.\d+)?)(cm3)", r"(\1*0.001)", self.element)
            self.element = re.sub(r"(\d+(\.\d+)?)(mm3)", r"(\1*0.000001)", self.element)
            self.element = re.sub(r"(\d+(\.\d+)?)(mol/dm3)", r"(\1*1)", self.element)
            self.element = re.sub(r"(\d+(\.\d+)?)(%)", r"(\1*0.01)", self.element)

            
            self.element = re.sub(r"([A-Z][a-z]?\d*(?:\.\d+)?)(\((.*?)\))", r"\1+\2", self.element)    
            print(self.element)    
            self.element = re.sub(r"(\d+(\.\d+)?)\((.*?)\)", r"\1*(\3)", self.element) 
            print(self.element)
            self.element = re.sub(r"([A-Z][a-z]?\d*(?:\.\d+)?)(?=[A-Z])", r"\1+", self.element)
            print(self.element)
            #self.element = re.sub(r"([a-z])([A-Z])", r"\1+\2", self.element)
            #print(self.element)   
            #self.element = re.sub(r"([A-Z])([A-Z])", r"\1+\2", self.element)  
            #print(self.element)
            self.element = re.sub(r"([A-Z][a-z]?)(\d+)", r"(\1*\2)", self.element)
            print(self.element)
            self.element = re.sub(r"(\)(\d+)?)([A-Z])", r"\1+\2", self.element)
            print(self.element)
            self.element = re.sub(r"(\))(\d+)", r"\1*\2", self.element)

            print(self.element)
            output2=self.element
            output1=eval(self.element)
            self.calculate_output_converted.configure(text=output2)
            self.calculate_output.configure(text=output1)
        except:
            self.calculate_output_converted.configure(text="Invalid Input")
            self.calculate_output.configure(text="")

    def info(self):
        """
        Creates an information window with details about the mole calculator.

        This function creates a new window using the `ctk.CTk` class and sets the title to "Info".
        The window size is set to 800x500 pixels. It then creates a frame within the window using
        the `ctk.CTkFrame` class and packs it. 

        Inside the frame, a label is created using the `ctk.CTkLabel` class. The label displays 
        information about the mole calculator, including instructions for inputting elements, 
        rules for using the calculator, and examples. The label is packed inside the frame.

        This function does not take any parameters and does not return any values.
        """
        info_window = ctk.CTk()
        info_window.title("Info")
        info_window.geometry("800x500")
        info_window_frame=ctk.CTkFrame(master=info_window)
        info_window_frame.pack()
        info_text = ctk.CTkLabel(master=info_window_frame, text="this is a mole calculator so inputted elements are their mass numbers (example: H2 is actually gonna be percieved as 2 as hydrogens mass number is 1)" + "\n" + "\n" +  "Rules: firstly you should enter the elm.element, then press the calculate button." + "\n" + "\n" + "Example: H2, then press the calculate button." + "\n" + "\n" + "Secondly, you should have the elm.element's chemical symbol correctly(example: NaCl and not nacl)" + "\n" + "\n" + "Thirdly, if there is more than one moles of a compound then input it like this (example: 5*(H2O))" + "\n" + "\n" + "You can write the word -const- to multiply the mass number by avagadros constant/6.022*(10**23)")
        info_text.pack()
    def history(self):
        history_window = ctk.CTk()
        history_window.title("History")
        history_window.geometry("800x500")
        history_window.configure(bg="black")
        history_window_frame=ctk.CTkFrame(master=history_window, bg="black")
        history_window_frame.pack()
        history_text = ctk.CTkLabel(master=history_window_frame, text=result_history)
        history_text.pack()



H = 1
He = 4
Li = 7
Be = 9
B = 11
C = 12
N = 14
O = 16
F = 19
Ne = 20
Na = 23
Mg = 24
Al = 27
Si = 28
P = 31
S = 32
Cl = 35.5
Ar = 40
K = 39
Ca = 40
Sc = 45
Ti = 48
V = 51
Cr = 52
Mn = 55
Fe = 56
Ni = 59
Co = 59
Cu = 64
Zn = 65
Ga = 70
Ge = 73
As = 75
Se = 79
Br = 80
Kr = 84
Rb = 85
Sr = 88
Y = 89
Zr = 91
Nb = 93
Mo = 96
Tc = 98
Ru = 101
Rh = 103
Pd = 106
Ag = 108
Cd = 112
In = 115
Sn = 119
Sb = 122
I = 127
Te = 128
Xe = 131
Cs = 133
Ba = 137
La = 139
Ce = 140
Pr = 141
Nd = 144
Pm = 145
Sm = 150
Eu = 152
Gd = 157
Tb = 159
Dy = 163
Ho = 165
Er = 167
Tm = 169
Yb = 173
Lu = 175
Hf = 178.5
Ta = 181
W = 184
Re = 186
Os = 190
Ir = 192
Pt = 195
Au = 197
Hg = 201
Tl = 204
Pb = 207
Bi = 208
Th = 232
Pa = 231
U = 238
Np = 237
Pu = 244
Am = 243
Cm = 247
Bk = 247
Cf = 251
Es = 252
Fm = 257
Md = 258
No = 259
Lr = 262
Rf = 267
Db = 270
Sg = 271
Bh = 270
Hs = 277
Mt = 276
Ds = 281
Rg = 280
Cn = 285
Nh = 284
Fl = 289
Mc = 288
Lv = 293
Ts = 294
Og = 294

app = App()