# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 20:14:08 2020

@author: M.Dhia
"""

# Importing the libraries

import ExcelManipulation as excel
import addNote as note
import knnAlgo as knn
import kmeansAlgo as kmeans

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter import filedialog
import os

#==================================VARIABLES==========================================

root =Tk()
root.title("POOPER : Papers Searching ")
root.resizable(False, False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

msg=""
listOfNotes=[]
dataset=""
#============================== Functions==============================================

def askOpenFileName():
    my_filetypes = [('all files', '.*'), ('text files', '.txt')]
    answer = filedialog.askopenfilename(parent=root,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=my_filetypes)
    input_file.insert(END, answer)
    
def noneFunc():
    return 0

def readFromTxt():
    file_name=variable1.get()
    counter=0
    with open(file_name, 'r') as f :
        reader=f.readlines()
        listOfNotes=reader
        print(listOfNotes)
        for i in range(len(listOfNotes)):
            counter=counter+1
        if(counter>=20):
            location=excel.location()
            excel.addLine(location, listOfNotes)
            T.insert(END, "okcls") 
        else:
            msg3="ya wildi yehdik rahoum 20  \n"
            T.insert(END, msg3)   
          
def algoKnn():
    print("URL FILE KNN "+excel.location())
    dataset = excel.readCSV(excel.location())
    list_result=knn.knnAlgo(dataset)  
    for i in range(len(list_result)):
        T.insert(END, list_result[i]+"\n")       
    excel.dropLastLine(dataset,excel.location())
    
def algoKmeans():
    print("MY CODE \n\n\n")
    j=0
    list_results=[]
    list_res=[]
    dataset = excel.readCSV(excel.location())
    list_results=kmeans.kmeansAlgo(dataset)
    for index, row in list_results.iterrows() :
        while (j<5):
            print(str(list_results.loc[j]))
            list_res.insert(j, str(list_results.loc[j]))
            j=j+1       
    print("your result "+str(list_res))
    for x in list_res: 
        x.replace('Name : ','')
        x.replace(', dtype: object','')
        x.replace('0','')
        x.replace('1','')
        x.replace('2','')
        x.replace('3','')
        x.replace('4','')
           
    for ii in range(len(list_res)): 
        T.insert(END,str(list_res[ii]))
    excel.dropLastLine(dataset,excel.location())
    
variable1 = StringVar()
#================================= Frames ==============================================

Top = Frame(root, width=300, height=50, bd=0, relief="raise")
Top.pack(side=TOP)

Left = Frame(root, width=900, height=x/3, bd=0, relief="raise")
Left.pack(side=LEFT)

Buttons = Frame(Top, width=900, height=50, bd=0, relief="raise")
Buttons.pack(side=BOTTOM)

#==================================BUTTONS AND LABEL WIDGET=====================================
btn_browser = Button(Buttons, width=10, text="Parcourir", command=askOpenFileName)
btn_browser.pack(side=LEFT)
input_file=Entry(Buttons, width=10, textvariable=variable1)
input_file.pack(side=LEFT)
btn_note = Button(Buttons, width=10, text="Insert", command=readFromTxt)
btn_note.pack(side=LEFT)
btn_knnn = Button(Buttons, width=10, text="Algo KNN", command=algoKnn)
btn_knnn.pack(side=LEFT)
btn_kmins = Button(Buttons, width=10, text="Algo KMEANS", command=algoKmeans)
btn_kmins.pack(side=LEFT)



S = Scrollbar(Left)
T = Text(Left, height=450, width=900)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
msg=msg+"------------- Hello -------------- \n---------- Welcome to ----------------------------------------------------------------------------    \n           the Papers Analyser.       "+"\n \n \n"+" 1 : We begin by downloading the relevant texts for each paper."+"\n"+"\n"+"To Start please Select Load Papers button \n\n"
T.insert(END, msg)




#################  K-MEANS ALGORITHME   ########################


##################  Drop Last Line IN EXCEL FILE  #############




#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()





