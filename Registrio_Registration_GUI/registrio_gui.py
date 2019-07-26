# Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from tkintertable import TableCanvas, TableModel
from tkinter import ttk

# Database
import sqlite3
import csv


conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS usersdata(firstname TEXT,lastname TEXT,email TEXT,age TEXT,date_of_birth TEXT,address TEXT,phonenumber REAL)')


def add_data(firstname,lastname,email,age,date_of_birth,address,phonenumber):
	c.execute('INSERT INTO usersdata(firstname ,lastname ,email ,age,date_of_birth,address,phonenumber ) VALUES (?,?,?,?,?,?,?)',(firstname,lastname,email,age,date_of_birth,address,phonenumber))
	conn.commit()


def view_all_users():
	c.execute('SELECT * FROM usersdata')
	data = c.fetchall()
	# for row in data:
	# 	print(row)
	# return data
	for row in data:
		print(row)
		tree.insert("", tk.END, values=row)
	# tab2_display.insert(tk.END,data)

def view_all_details():
	c.execute('SELECT * FROM usersdata')
	data = c.fetchall()
	# for row in data:
	# 	print(row)
	# return data
	for row in data:
		# print(row)
		# tree.insert("", tk.END, values=row)
		tab2_display.insert("",tk.END,row)	

def get_single_user(firstname):
	c.execute('SELECT * FROM usersdata WHERE firstname="{}"'.format(firstname))
	data = c.fetchall()
	# tab2_display.insert(tk.END,data)
	return data

def edit_single_user(firstname,new_name):
	c.execute('UPDATE usersdata SET firstname ="{}" WHERE firstname="{}"'.format(new_name,firstname
		))
	conn.commit()
	data = c.fetchall()
	return data
def delete_single_user(firstname):
	c.execute('DELETE FROM usersdata WHERE firstname="{}"'.format(firstname))
	conn.commit()


def view_all_data():
	c.execute('SELECT * FROM usersdata')
	data = c.fetchall()
	# for row in data:
	# 	print(row)
	# result = [ row for row in data ]
	# return result
	
	


create_table()

 # Structure and Layout
window = Tk()
window.title("Registrio GUI")
window.geometry("750x450")
window.config(background='black')

style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn',)


# TAB LAYOUT
tab_control = ttk.Notebook(window,style='lefttab.TNotebook')
 
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Home":^20s}')
tab_control.add(tab2, text=f'{"View":^20s}')
tab_control.add(tab3, text=f'{"Search":^20s}')
tab_control.add(tab4, text=f'{"Edit":^20s}')
tab_control.add(tab5, text=f'{"Export":^20s}')
tab_control.add(tab6, text=f'{"About ":^20s}')


label1 = Label(tab1, text= 'Registrio GUI',padx=5, pady=5)
label1.grid(column=0, row=0)
 
label2 = Label(tab2, text= 'View',padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text= 'Search',padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab4, text= 'Edit/Update',padx=5, pady=5)
label4.grid(column=0, row=0)

label5 = Label(tab5, text= 'Export',padx=5, pady=5)
label5.grid(column=0, row=0)

label6 = Label(tab6, text= 'About',padx=5, pady=5)
label6.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')


# Functions
def clear_text():
	entry_fname.delete('0',END)
	entry_lname.delete('0',END)
	entry_email.delete('0',END)
	entry_age.delete('0',END)
	entry_address.delete('0',END)
	entry_phone.delete('0',END)

def add_details():
	firstname = str(entry_fname.get())
	lastname = str(entry_lname.get())
	email = str(entry_email.get())
	age = str(entry_age.get())
	date_of_birth = str(cal.get())
	phone_number = str(entry_phone.get())
	address = str(entry_address.get())
	add_data(firstname,lastname,email,age,date_of_birth,address,phone_number)
	result = '\nFirst Name:{},\nLast Name:{},\nEmail:{},\nAge:{},\nDate of Birth:{},\nPhone Number:{},\nAddress:{}\n'.format(firstname,lastname,email,age,date_of_birth,phone_number,address)
	tab1_display.insert(tk.END,result)
	messagebox.showinfo(title = "Registrio GUI", message = "Submitted to DataBase")

def clear_display_result():
	tab1_display.delete('1.0',END)


def search_user_by_name():
	firstname = str(entry_search.get())
	result = get_single_user(firstname)
	# c.execute('SELECT * FROM usersdata WHERE firstname="{}"'.format(firstname))
	# data = c.fetchall()
	# print(result)
	tab2_display.insert(tk.END,result)


def clear_display_view():
	tab2_display.delete('1.0',END)


def clear_entered_search():
	entry_search.delete('0',END)

def clear_tree_view():
	# tab2_display.delete('1.0',END)
	tree.delete('1.0',END)


def export_as_csv():
	filename = str(entry_filename.get())
	myfilename = filename + '.csv'
	with open(myfilename, 'w') as f:
	    writer = csv.writer(f)
	    c.execute('SELECT * FROM usersdata')
	    data = c.fetchall()
	    writer.writerow(['firstname','lastname','email','age','date_of_birth','address','phonenumber'])
	    writer.writerows(data)
	    messagebox.showinfo(title = "Registrio GUI", message = '"Exported As {}"'.format(myfilename))

def export_as_xls():
	pass




# Main Home Registration
l1 = Label(tab1,text="First Name",padx=5,pady=5)
l1.grid(column=0,row=1)
fname_raw_entry = StringVar()
entry_fname = Entry(tab1,textvariable=fname_raw_entry,width=50)
entry_fname.grid(row=1,column=1)

l2 = Label(tab1,text="Last Name",padx=5,pady=5)
l2.grid(column=0,row=2)
lname_raw_entry = StringVar()
entry_lname = Entry(tab1,textvariable=lname_raw_entry,width=50)
entry_lname.grid(row=2,column=1)

l3 = Label(tab1,text="Email",padx=5,pady=5)
l3.grid(column=0,row=3)
email_raw_entry = StringVar()
entry_email = Entry(tab1,textvariable=email_raw_entry,width=50)
entry_email.grid(row=3,column=1)


l4 = Label(tab1,text="Age",padx=5,pady=5)
l4.grid(column=0,row=4)
raw_entry = IntVar()
entry_age = Entry(tab1,textvariable=raw_entry,width=50)
entry_age.grid(row=4,column=1)

l5 = Label(tab1,text="Date of Birth",padx=5,pady=5)
l5.grid(column=0,row=5)
dob_raw_entry = StringVar()
cal = DateEntry(tab1, width=30,textvariable=dob_raw_entry, background='darkblue',foreground='white', borderwidth=2, year=2010)
cal.grid(row=5,column=1,padx=10, pady=10)


l6 = Label(tab1,text="Address",padx=5,pady=5)
l6.grid(column=0,row=6)
address_raw_entry = StringVar()
entry_address = Entry(tab1,textvariable=address_raw_entry,width=50)
entry_address.grid(row=6,column=1)


l7 = Label(tab1,text="Phone Number",padx=5,pady=5)
l7.grid(column=0,row=7)
phone_raw_entry = StringVar()
entry_phone = Entry(tab1,textvariable=phone_raw_entry,width=50)
entry_phone.grid(row=7,column=1)

button1 = Button(tab1,text="Clear",width=12,bg='#03A9F4',fg='#fff',command=clear_text)
button1.grid(row=8,column=0,padx=10,pady=10)


button2 = Button(tab1,text="Add",width=12,bg='#03A9F4',fg='#fff',command=add_details)
button2.grid(row=8,column=1,padx=10,pady=10)


# Display Screen For Result
tab1_display = ScrolledText(tab1,height=5)
tab1_display.grid(row=10,column=0, columnspan=3,padx=5,pady=5)
button3 = Button(tab1,text="Clear Result",width=12,bg='#03A9F4',fg='#fff',command=clear_display_result)
button3.grid(row=12,column=1,padx=10,pady=10)


# View 
# label_view1 = Label(tab2,text="Search Name",padx=5,pady=5)
# label_view1.grid(column=0,row=2)
# search_raw_entry = StringVar()
# entry_search = Entry(tab2,textvariable=search_raw_entry,width=30)
# entry_search.grid(row=2,column=1)

button_view2 = Button(tab2,text="View All",width=12,bg='#03A9F4',fg='#fff',command=view_all_users)
button_view2.grid(row=1,column=0,padx=10,pady=10)

# button_view3 = Button(tab2,text="Clear Search",width=12,bg='#03A9F4',fg='#fff',command=clear_entered_search)
# button_view3.grid(row=1,column=1,padx=10,pady=10)

# button_view4 = Button(tab2,text="Clear Results",width=12,bg='#03A9F4',fg='#fff',command=clear_tree_view)
# button_view4.grid(row=1,column=2,padx=10,pady=10)

# button_view5 = Button(tab2,text="Search",width=12,bg='#03A9F4',fg='#fff',command=search_user_by_name)
# button_view5.grid(row=2,column=2,padx=10,pady=10)


tree= ttk.Treeview(tab2, column=("column1", "column2", "column3","column4", "column5","column6", "column7"), show='headings')
tree.heading("#1", text="First Name")
tree.heading("#2", text="Last Name")
tree.heading("#3", text="")
tree.heading("#1", text="NUMBER")
tree.heading("#2", text="FIRST NAME")
tree.heading("#3", text="SURNAME")
tree.heading('#7',text="Phone Number")
tree.grid(row=10,column=0, columnspan=3,padx=5,pady=5)

# Search
label_view1 = Label(tab3,text="Search Name",padx=5,pady=5)
label_view1.grid(column=0,row=1)
search_raw_entry = StringVar()
entry_search = Entry(tab3,textvariable=search_raw_entry,width=30)
entry_search.grid(row=1,column=1)

# button_view2 = Button(tab3,text="View All",width=12,bg='#03A9F4',fg='#fff',command=view_all_details)
# button_view2.grid(row=1,column=0,padx=10,pady=10)

button_view3 = Button(tab3,text="Clear Search",width=12,bg='#03A9F4',fg='#fff',command=clear_entered_search)
button_view3.grid(row=2,column=1,padx=10,pady=10)

button_view4 = Button(tab3,text="Clear Results",width=12,bg='#03A9F4',fg='#fff',command=clear_display_view)
button_view4.grid(row=2,column=2,padx=10,pady=10)

button_view5 = Button(tab3,text="Search",width=12,bg='#03A9F4',fg='#fff',command=search_user_by_name)
button_view5.grid(row=1,column=2,padx=10,pady=10)

tab2_display = ScrolledText(tab3,height=5)
# tab2_display = Listbox(tab2,height=5,width=60)
tab2_display.grid(row=10,column=0, columnspan=3,padx=5,pady=5)
# tree= ttk.Treeview(tab3, column=("column1", "column2", "column3","column4", "column5","column6", "column7"), show='headings')
# tree.heading("#1", text="First Name")
# tree.heading("#2", text="Last Name")
# tree.heading("#3", text="")
# tree.heading("#1", text="NUMBER")
# tree.heading("#2", text="FIRST NAME")
# tree.heading("#3", text="SURNAME")
# tree.heading('#7',text="Phone Number")
# tree.grid(row=10,column=0, columnspan=3,padx=5,pady=5)


# Export Database

label_export1 = Label(tab5,text="File Name",padx=5,pady=5)
label_export1.grid(column=0,row=2)
filename_raw_entry = StringVar()
entry_filename = Entry(tab5,textvariable=filename_raw_entry,width=30)
entry_filename.grid(row=2,column=1)

button_export3 = Button(tab5,text="To CSV",width=12,bg='#03A9F4',fg='#fff',command=export_as_csv)
button_export3.grid(row=3,column=1,padx=10,pady=10)

button_export3 = Button(tab5,text="To XLS",width=12,bg='#03A9F4',fg='#fff',command=export_as_xls)
button_export3.grid(row=3,column=2,padx=10,pady=10)


data = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},
       'rec2': {'col1': 99.88, 'col2': 108.79, 'label': 'rec2'}
       }
# data2 = view_all_data()
table = TableCanvas(tab4,data=data)
table.show()


# About TAB
about_label = Label(tab6,text="Registrio GUI V.0.0.1 \n Jesus saves @JCharisTech",pady=5,padx=5)
about_label.grid(column=0,row=1)



window.mainloop()


# Jesus Saves @JCharisTech
# By Jesse E.Agbe(JCharis)