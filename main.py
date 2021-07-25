import mysql.connector 
from datetime import datetime 
from tkinter import ttk
import tkinter as tk
from tkinter import *

def ViewMask(mask):
    sql_select_Query1 = "select * from information where MASK = 1"
    sql_select_Query2 = "select * from information where MASK = 0"
    if( mask==True):
        mycursor.execute(sql_select_Query1)
    else:
        mycursor.execute(sql_select_Query2)
    # get all records
    mydata=[]
    mydata = mycursor.fetchall()
    mydb.commit()
    for i in tree.get_children():
        tree.delete(i)
    for row in mydata:
        #print(row) 
        tree.insert("", tk.END, values=row) 
    var.set('Total: '+str(len(tree.get_children())))        
    top.update()
    return 1
def DateTime(eventObject):
    sql_select_Query3 = "select * from information where DATE_TIME LIKE '{0:s}%'".format(eventObject.widget.get())
    mycursor.execute(sql_select_Query3)
    mydata=[]
    mydata = mycursor.fetchall()
    mydb.commit()
    for i in tree.get_children():
        tree.delete(i)
    for row in mydata:
        #print(row) 
        tree.insert("", tk.END, values=row) 
    var.set('Total: '+str(len(tree.get_children())))        
    top.update()
#Create the connection object   
mydb = mysql.connector.connect(host = "[your_ip_addr]", user = "[enter_your_user_name]",passwd = "[enter_your_password]", database='coronavirus_system',port=3312)  
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS information")
mycursor.execute ("CREATE TABLE information (PERSON_ID INT NOT NULL AUTO_INCREMENT, MASK BOOLEAN, DATE_TIME DATETIME, PRIMARY KEY(PERSON_ID))")
filename = "metadata.txt"
with open(filename) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip().split() for x in content] 
# print (content)
value = [[x[0]+' '+x[1], x[4], x[7]] for x in content if(len(x)>0)]
new_value =[]


for x in value:
    for i in range(int(x[1])):
        new_value.append(['0',x[0]])
    for j in range(int(x[2])):
        new_value.append(['1',x[0]])  
sql = "INSERT INTO information (MASK, DATE_TIME) VALUES (%s, %s)"        
for x in new_value:
    mycursor.execute(sql, x)     
sql_select_Query = "select * from information"
mycursor.execute(sql_select_Query)
# get all records
records = mycursor.fetchall()
#print("Total number of rows in table: ", mycursor.rowcount)
#print(records)
mydb.commit()

top = tk.Tk()
top.title('Mask Detection System')
top.geometry("800x400")

#for i in range(total_rows):
#    for j in range(total_columns):
#        e = Entry(top, width=20, fg='black',
#                       font=('Arial',10,'bold'))
#        e.grid(row=i, column=j, sticky='news')
#        e.insert(END, data[i][j])
# Set name and position for columns
tree = ttk.Treeview(top, column=("c1", "c2", "c3"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="PERSON_ID")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="MASK")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="DATE_TIME")

for row in records:
        #print(row) 
        tree.insert("", tk.END, values=row) 
tree.grid(row=0,column=0, columnspan=2)
tree.grid_rowconfigure(0, weight=1)
var = StringVar()
label = Label( top, textvariable=var)
var.set('Total: '+str(len(tree.get_children())))
label.grid(row=1, column=0,columnspan=2)
button1 = tk.Button(text="Display All Mask Data", command = lambda:ViewMask(True))
button1.grid(row=2, column=0)
button2 = tk.Button(text="Display All No Mask Data", command = lambda:ViewMask(False))
button2.grid(row=2, column=1)

time = set([x[2].strftime('%Y-%m-%d') for x in records])
time_data =[str(x) for x in time]
#print(time_data)
box_value = StringVar()
w = ttk.Combobox(top, values = time_data)
w.current(0)
w.bind("<<ComboboxSelected>>",  DateTime)
w.grid(row=2, column=2)

top.mainloop()  

