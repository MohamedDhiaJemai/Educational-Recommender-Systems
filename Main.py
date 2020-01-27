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
root.title("Système de Recommandation de Cours")
root.resizable(False, False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1300
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

msg=""
listOfNotes=[]
dataset=""
tt=0
tt=0
#============================== Functions==============================================

def askOpenFileName():
    my_filetypes = [('all files', '.*'), ('text files', '.xlsx')]
    answer = filedialog.askopenfilename(parent=root,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=my_filetypes)
    input_file.insert(END, answer)
    
def noneFunc():
    return 0

def readFromTxt():
    file_name=variable1.get()
    if(file_name ==""):
        msg3="\n \n \n      4 : Vous Devez cliquer sur le button PARCOURIR et inserer le fichier des notes de l etudiant cible."
        T.insert(END, msg3)        
    else:
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
                T.insert(END, "\n \n \n      4 : Insertion Des Notes Effectuer Avec Succes") 
            else:
                msg3="\n \n \n      4 : Insertion Des Notes Effectuer Avec Succes \n \n \n      5 : Cliquer Sur le button RECOMMANDATION KNN ou bien RECOMMANDATION K-MEANS."
                T.insert(END, msg3)   
          
def algoKnn():
    if(vv.get()==""):
        ttt=-1
    else:
        ttt=int(vv.get())
    print("ttt",ttt)
    if (ttt==-1):
        msg4="\n \n \n      4 : Impossible De Tourner l'algorithme : Vous Dever verifier le Neighbors. "
        T.insert(END, msg4)
        print("impossible")
    elif(ttt<=1):
        msg4 = "\n \n \n      Vous devez entrer un nombre Neighbors supérieur à 1 "
        T.insert(END, msg4)
    else:
        msg3="\n \n \n      RECOMMANDATION PAR KNN :\n \n \n"
        T.insert(END, msg3)
        print("URL FILE KNN "+excel.location())
        dataset = excel.readCSV(excel.location())
        list_result=knn.knnAlgo(dataset,ttt)
        for i in range(len(list_result)):
            T.insert(END,list_result[i]+"\n")       
        excel.dropLastLine(dataset,excel.location())
        input_file.delete(0,'end')
    
def algoKmeans():
    print("MY CODE \n\n\n")
    print("Nombre de clusteur donnée = ",v.get())
    print("\n")
    if(v.get()==""):
        tt=-1
    else:
        tt=int(v.get())
    print("tt",tt)
    if (tt==-1):
        msg4="\n \n \n      4 : Impossible De Tourner l'algorithme : Vous Dever verifier le Nombre de cluster K. "
        T.insert(END, msg4)
        print("impossible")
    elif(tt<=1):
        msg4 = "\n \n \n      Vous devez entrer un nombre de clusteur supérieur à 1 "
        T.insert(END, msg4)
    else:
        msg3="\n \n \n      RECOMMANDATION PAR K-MEANS :"
        T.insert(END, msg3)
        j=0
        list_results=[]
        list_res=[]
        dataset = excel.readCSV(excel.location())
        list_results=kmeans.kmeansAlgo(dataset,v.get())
        for index, row in list_results.iterrows() :
            while (j<5):
                print(str(list_results.loc[j]))
                list_res.insert(j, str(list_results.loc[j]))
                j=j+1       
        #print("your result "+str(list_res))
#        for x in list_res:
#            print(x)
#            x.replace('Name : ','')
#            x.replace(' dtype: objectindex','')
#            x.replace('index ','')
#            x.replace('0','')
#            x.replace('1','')
#            x.replace('2','')
#            x.replace('3','')
#            x.replace('4','')
                
        for ii in range(len(list_res)):
            T.insert(END,str(list_res[ii]))
        excel.dropLastLine(dataset,excel.location())
        input_file.delete(0,'end')
    
variable1 = StringVar()
#================================= Frames ==============================================

Top = Frame(root, width=300, height=50, bd=0, relief="raise")
Top.pack(side=TOP)

Left = Frame(root, width=900, height=x/3, bd=0, relief="raise")
Left.pack(side=LEFT)

Buttons = Frame(Top, width=900, height=50, bd=0, relief="raise",padx=10,pady=10)
Buttons.pack(side=BOTTOM)

Buttons1 = Frame(Buttons, width=900, height=50, bd=1, relief="raise",padx=15,pady=10)
Buttons1.pack(side=LEFT, padx=6)


Buttons2 = Frame(Buttons, width=900, height=50, bd=1, relief="raise",padx=15,pady=10)
Buttons2.pack(side=LEFT, padx=6)

Buttons3 = Frame(Buttons, width=900, height=50, bd=1, relief="raise",padx=15,pady=10)
Buttons3.pack(side=LEFT, padx=6)

#==================================BUTTONS AND LABEL WIDGET=====================================

label=Label(Buttons1, width= 30, text = "Entrée Des Données : ",font='Helvetica 14 bold' ,padx=5,pady=6)
label.pack(side=TOP)

btn_browser = Button(Buttons1, width=10, text="Parcourir", command=askOpenFileName)
btn_browser.pack(side=LEFT)

x=Label(Buttons1, width= 2, text = "")
x.pack(side=LEFT)

input_file=Entry(Buttons1, width=30, textvariable=variable1)
input_file.pack(side=LEFT)

x=Label(Buttons1, width= 2, text = "")
x.pack(side=LEFT)

btn_note = Button(Buttons1, width=10, text="Insert", command=readFromTxt)
btn_note.pack(side=LEFT)



label=Label(Buttons2, width= 30, text = "Recommandation Par KNN : ",font='Helvetica 14 bold' ,padx=5,pady=6)
label.pack(side=TOP)

btn_knnn = Button(Buttons2, width=25, text="ALGORITHME  KNN", command=algoKnn)
btn_knnn.pack(side=LEFT)

label=Label(Buttons2, width= 14, text = "N Neighbors : ")
label.pack(side=LEFT)

vv = StringVar()
nbrCluster=Entry(Buttons2, width=5,textvariable=vv)
nbrCluster.pack(side=LEFT)



#x=Label(Buttons, width= 8, text = "")
#x.pack(side=LEFT)

label=Label(Buttons3, width= 30, text = "Recommandation Par K-MEANS : ",font='Helvetica 14 bold' ,padx=5,pady=6)
label.pack(side=TOP)

btn_kmins = Button(Buttons3, width=25, text="ALGORITHME K-MEANS", command=algoKmeans)
btn_kmins.pack(side=LEFT)

label=Label(Buttons3, width= 12, text = "N Clusters : ")
label.pack(side=LEFT)

v = StringVar()
nbrCluster=Entry(Buttons3, width=5,textvariable=v)
nbrCluster.pack(side=LEFT)








S = Scrollbar(Left)
T = Text(Left, height=450, width=900, font='Helvetica 10 bold')
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set,)
msg=msg+"\n-------------------------------------------------------------------------------------------------------------------------------------------------- BIENVENUE -------------------------------------------------------------------------------------------------------------------------------------------------------- \n \n \n---------------------------------------------------------------------------------------------------------------------------- SYSTEME DE RECOMMANDATION DE COURS ---------------------------------------------------------------------------------------------------------------------------   \n   "+"\n \n"+"      1 : Pour Commencer Vous Devez cliquer sur le boutton PARCOURIR \n "+"\n"+"\n"+"      2 : Importer le fichier qui contien la liste des notes de etudiant cible \n \n \n      3 : cliquer sur Insertion."
T.insert(END, msg)




#################  K-MEANS ALGORITHME   ########################


##################  Drop Last Line IN EXCEL FILE  #############




#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()





