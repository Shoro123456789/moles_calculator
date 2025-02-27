import tkinter as tk
import re # import regular expression library 
from tkinter import END
my_w = tk.Tk()
my_w.geometry("410x400")  # Size of the window 
my_w.title("plus2net.com")  # Adding a title
font1=('Times',24,'bold') # font size and style 
l0=tk.Label(text='Autocomplete',font=font1) # adding label at top
l0.grid(row=0,column=1) 
# data source list,
my_list=['aecde','adba','acbd','abcd','abded', 
       'bdbd','baba','bcbc','bdbd']

def my_upd(my_widget): # On selection of option 
    my_w = my_widget.widget
    index = int(my_w.curselection()[0]) # position of selection
    value = my_w.get(index) # selected value 
    e1_str.set(value) # set value for string variable of Entry 
    l1.delete(0,END)     # Delete all elements of Listbox
def my_down(my_widget): # down arrow is clicked 
    l1.focus()  # move focus to Listbox
    l1.selection_set(0) # select the first option 
    
e1_str=tk.StringVar()  # string variable   
e1=tk.Entry(my_w,textvariable=e1_str,font=font1) # entry    
e1.grid(row=1,column=1,padx=10,pady=0)
# listbox 
l1 = tk.Listbox(my_w,height=6,font=font1,relief='flat',
    bg='SystemButtonFace',highlightcolor= 'SystemButtonFace')
l1.grid(row=2,column=1) 

def get_data(*args): # populate the Listbox with matching options 
    search_str=e1.get() # user entered string 
    l1.delete(0,END)     # Delete all elements of Listbox
    for element in my_list:
        if(re.match(search_str,element,re.IGNORECASE)):
            l1.insert(tk.END,element)#add matching options to Listbox
#l1.bind('<<ListboxSelect>>', my_upd)
e1.bind('<Down>', my_down) # down arrow key is pressed
l1.bind('<Right>', my_upd) # right arrow key is pressed
l1.bind('<Return>', my_upd)# return key is pressed 
e1_str.trace('w',get_data) #    
#print(my_w['bg']) # reading background colour of window 
my_w.mainloop()  # Keep the window open