import fire
import sqlite3
from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()



conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS notestable(author TEXT,title TEXT,message TEXT)')


def add_data(author,title,message):
	c.execute('INSERT INTO notestable(author,title,message) VALUES (?,?,?)',(author,title,message))
	conn.commit()


def view_all_notes():
	c.execute('SELECT * FROM notestable')
	data = c.fetchall()
	# for row in data:
	# 	print(row)
	return data

def get_single_note(title):
	c.execute('SELECT * FROM notestable WHERE title="{}"'.format(title))
	data = c.fetchall()
	return data


def get_note_by_title(title):
	c.execute('SELECT * FROM notestable WHERE title="{}"'.format(title))
	data = c.fetchall()
	return data

def get_note_by_author(author):
	c.execute('SELECT * FROM notestable WHERE author="{}"'.format(author))
	data = c.fetchall()
	return data
 

def get_note_by_msg(message):
	c.execute("SELECT * FROM notestable WHERE message like '%{}%'".format(message))
	data = c.fetchall()
	return data

def edit_note_author(author,new_author):
	c.execute('UPDATE notestable SET author ="{}" WHERE author="{}"'.format(new_author,author))
	conn.commit()
	data = c.fetchall()
	return data

def edit_note_title(title,new_title):
	c.execute('UPDATE notestable SET title ="{}" WHERE title="{}"'.format(new_title,title
		))
	conn.commit()
	data = c.fetchall()
	return data


def edit_note_msg(message,new_message):
	c.execute('UPDATE notestable SET title ="{}" WHERE title="{}"'.format(new_message,message
		))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(title):
	c.execute('DELETE FROM notestable WHERE title="{}"'.format(title))
	conn.commit()


# Main Commands
def add_note(author,title,message):
	""" Add A New Notes

	eg. python terminotes.py add-note --author Jesse --title "Simple Terminal Notes" --message "A simple note taking cli"


	eg. python terminotes.py add-note -a JCharis -t "Best Notes" -msg "This is secret"

	"""

	print("==============================")
	print(colored('Author:: {}'.format(author),'white','on_blue'))
	print(colored('Title:: {}'.format(title),'white','on_blue'))
	print(colored('Message:: {}'.format(message),'white','on_blue'))

	print("========Summary===============")
	from terminaltables import AsciiTable
	user_notes = [
		['Notes Info','Details'],
		['Title:',title],
		['Author:',author],
		['Message Length:',len(message)],
	
	]

	create_table()
	add_data(author,title,message)
	table1 = AsciiTable(user_notes)

	print(table1.table)
	print('Saved Notes To DataBase')

def show_all():
	""" Show All Notes  
	eg. python fterminotes.py show-all
	
	"""
	print("Showing All Notes")
	print("==============================")
	from terminaltables import AsciiTable
	result = view_all_notes()
	new_result = ['Author','Title','Message']
	print('{}'.format(new_result))
	table1 = AsciiTable(result)
	print(table1.table)


def view_note(title):
	""" View Note By Title 
	
	eg.	python fterminotes.py view-note --title "Best Notes"

	eg.  python fterminotes.py view-note -t "Best Notes"

	"""
	print("Searched For {}".format(title))
	from terminaltables import AsciiTable
	result = get_single_note(title)
	table1 = AsciiTable(result)
	print(table1.table)


def search(text,by):
	""" Search Note By Options [Title or Author]

	eg  terminotes.py search "Jesse" -by="title"

	 """
	print("Searched For :: {}".format(text))
	from terminaltables import AsciiTable
	if by == 'title':
		result = get_note_by_title(text)
		table1 = AsciiTable(result)
		print(table1.table)
	elif by == 'author':
		result = get_note_by_author(text)
		table1 = AsciiTable(result)
		print(table1.table)
	elif by == 'message':
		result = get_note_by_msg(text)
		table1 = AsciiTable(result)
		print(table1.table)
	else:
		print("{} Not a Choice ,Pls Try either of these [title/author/message]".format(by))


def edit_note(field,old,new):
	""" Edit Note By Field[title/author/message] 

	eg. python fterminotes.py edit-note --field="author" --old="Jesse" --new="JCharis" 

	"""
	print('Editing Field:: {} with {} and Updating to {}'.format(field,old,new))
	from terminaltables import AsciiTable

	print("===========Previous==============")
	result2 = view_all_notes()
	new_result = ['Author','Title','Message']
	print('{}'.format(new_result))
	table2 = AsciiTable(result2)
	print(table2.table)


	if field == 'title':
		result = edit_note_title(old,new)
		table1 = AsciiTable(result)
		print(table1.table)
	if field == 'author':
		result = edit_note_author(old,new)
		table1 = AsciiTable(result)
		print(table1.table)
	if field == 'message':
		result = edit_note_message(old,new)
		table1 = AsciiTable(result)
		print(table1.table)


	print("==========Updated===============")
	result3 = view_all_notes()
	new_result2 = ['Author','Title','Message']
	print('{}'.format(new_result2))
	table3 = AsciiTable(result3)
	print(table3.table)


def delete_note(title):
	""" Delete Note By Title 

	eg. python fterminote.py delete-note --title "Best Notes"

	"""
	print('Deleting :: {} '.format(title))
	from terminaltables import AsciiTable

	print("===========Previous==============")
	result2 = view_all_notes()
	new_result = ['Author','Title','Message']
	print('{}'.format(new_result))
	table2 = AsciiTable(result2)
	print(table2.table)

	result = delete_data(title)
	print("Deleted From DataBase")

def version():
	# then use Termcolor for all colored text output
	print(colored("Firenotes, 0.01",'white', 'on_red'))
	print(colored("Author: Jesse E. Agbe(JCharis)",'white', 'on_yellow'))
	print(colored("Jesus Saves @JCharisTech",'white', 'on_green'))


if __name__ == '__main__':
	fire.Fire({
		'add-note':add_note,
		'show-all':show_all,
		'view-note':view_note,
		'search':search,
		'edit-note':edit_note,
		'delete-note':delete_note,
		'version':version

		})



