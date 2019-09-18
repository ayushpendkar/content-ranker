#!/usr/bin/env python
# coding: utf-8

# In[10]:




import tkinter as tk  
from tkinter import ttk 
import pandas as pd
import easygui
import re
win = tk.Tk()  
# Application Name  
win.title("Content Ranker")  
win.geometry('500x500')  
# Label  
lbl = ttk.Label(win, text = "Enter the Content:").grid(column = 0, row = 0)  
def clicked():
    con=name.get()
    con1=str(con)
    data=easygui.fileopenbox()
    df1=pd.read_csv(data)
    df = df1[df1.Comp != 0]
    vol=list(df.Vol)
    comp=list(df.Comp)
    key=list(df.Keyword)
    ratio=[]
    for k in range(len(vol)):
        ratio.append(vol[k]/comp[k])
    max1=max(ratio)
    print(max1)
    for i in range(len(ratio)):
        if(ratio[i]==max1):
            key1=key[i]
    print(max1)
    print(key1)
    
   
    print(key1)
    if re.search(key1,con1):
            lbl2 = ttk.Label(win, text = "Content Passed the search Algorithm").grid(column = 0, row = 4)
    else:
            lbl3 = ttk.Label(win, text = "Change Content").grid(column = 0, row = 4)
    lbl4 = ttk.Label(win, text = "Ranking Keyword : "+key1).grid(column = 0, row = 6)
    lbl5 = ttk.Label(win, text = "With Search Volume to competition ratio : "+str(max1)).grid(column = 0, row = 8)
    
   
    


# Textbox widget  
name = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 60, textvariable = name).grid(column = 0, row = 1)
button1 = ttk.Button(win, text = "Submit", command = clicked).grid(column = 1, row = 1)  

# Button widget  


win.mainloop()  


# In[ ]:





# In[ ]:




