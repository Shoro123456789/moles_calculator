import re
import tkinter as tk
import customtkinter as ctk
from tkinter.font import Font
from tkinter import ttk
const = 6.022*(10**23)
gas = 24
window=tk.Tk()
bold_font = ctk.CTkFont(family="Helvetica", size=13, weight="bold")
window.title("Element Calculator")
window.geometry("250x135")
window.configure(bg="black")
frame1=tk.Frame(master=window, bg="black")
frame1.pack()
calculate_input = ctk.CTkEntry(master=frame1, width=180, font=bold_font)
calculate_input.pack()
result_history = ""

"""
This function calculates the output of the 
checmical formula provided by the user.
"""
def calculate():
    element = calculate_input.get()
    element = re.sub(r" ", r"", element)
    element = re.sub(r"(\d+(\.\d+)?)(g)", r"(\1*1)", element)
    element = re.sub(r"(\d+(\.\d+)?)(mg)", r"(\1*0.001)", element)
    element = re.sub(r"(\d+(\.\d+)?)(Kg)", r"(\1*1000)", element, flags=re.IGNORECASE)
    element = re.sub(r"(\d+(\.\d+)?)(Tonnes)", r"(\1*1000000)", element, flags=re.IGNORECASE)
    element = re.sub(r"(\d+(\.\d+)?)(dm3)", r"(\1*1)", element)
    element = re.sub(r"(\d+(\.\d+)?)(cm3)", r"(\1*0.001)", element)
    element = re.sub(r"(\d+(\.\d+)?)(mm3)", r"(\1*0.000001)", element)
    element = re.sub(r"(\d+(\.\d+)?)(mol/dm3)", r"(\1*1)", element)
    element = re.sub(r"(\d+(\.\d+)?)(%)", r"(\1*0.01)", element)

    
    element = re.sub(r"([A-Z][a-z]?\d*(?:\.\d+)?)(\((.*?)\))", r"\1+\2", element)    
    print(element)    
    element = re.sub(r"(\d+(\.\d+)?)\((.*?)\)", r"\1*(\3)", element) 
    print(element)
    element = re.sub(r"([A-Z][a-z]?\d*(?:\.\d+)?)(?=[A-Z])", r"\1+", element)
    print(element)
    #element = re.sub(r"([a-z])([A-Z])", r"\1+\2", element)
    #print(element)   
    #element = re.sub(r"([A-Z])([A-Z])", r"\1+\2", element)  
    #print(element)
    element = re.sub(r"([A-Z][a-z]?)(\d+)", r"(\1*\2)", element)
    print(element)
    element = re.sub(r"(\)(\d+)?)([A-Z])", r"\1+\2", element)
    print(element)
    element = re.sub(r"(\))(\d+)", r"\1*\2", element)

    print(element)
    output2=element
    output1=eval(element)
    calculate_output_converted.config(text=output2)
    calculate_output.config(text=output1)
    result_history += output2 + "=" + str(output1) + "\n"
def info():
    info_window = tk.Tk()
    info_window.title("Info")
    info_window.geometry("800x500")
    info_window.configure(bg="black")
    info_window_frame=tk.Frame(master=info_window, bg="black")
    info_window_frame.pack()
    info_text = tk.Label(master=info_window_frame, text="this is a mole calculator so inputted elements are their mass numbers (example: H2 is actually gonna be percieved as 2 as hydrogens mass number is 1)" + "\n" + "\n" +  "Rules: firstly you should enter the element, then press the calculate button." + "\n" + "\n" + "Example: H2, then press the calculate button." + "\n" + "\n" + "Secondly, you should have the element's chemical symbol correctly(example: NaCl and not nacl)" + "\n" + "\n" + "Thirdly, if there is more than one moles of a compound then input it like this (example: 5*(H2O))" + "\n" + "\n" + "You can write the word -const- to multiply the mass number by avagadros constant/6.022*(10**23)", bg="black", fg="white")
    info_text.pack()
def history():
    history_window = tk.Tk()
    history_window.title("History")
    history_window.geometry("800x500")
    history_window.configure(bg="black")
    history_window_frame=tk.Frame(master=history_window, bg="black")
    history_window_frame.pack()
    history_text = tk.Label(master=history_window_frame, text=result_history, bg="black", fg="white")
    history_text.pack()


calculate_button = ctk.CTkButton(master=frame1, text="Calculate", command=calculate, width=15)
calculate_button.pack()
info = ctk.CTkButton(master=frame1, text="Info", command=info, width=15)
info.pack()
history = ctk.CTkButton(master=frame1, text="History", command=history, width=15)
#history.pack()
calculate_output_converted = tk.Label(master=frame1, bg="black", fg="white")
calculate_output = tk.Label(master=frame1, bg="black", fg="white")
calculate_output_converted.pack()
calculate_output.pack()
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


window.mainloop()