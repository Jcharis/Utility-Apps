import click
import click_config_file
from click_didyoumean import DYMGroup
import sqlite3

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


@click.group(cls=DYMGroup)
@click.version_option(version='0.01',prog_name='termipad')
def main():
	""" Termipad : A simple notes taking CLI  

	"""
	pass


@main.command()
@click.option('--author','-a',prompt=True)
@click.option('--title','-t',prompt=True)
@click.option('--message','-msg',prompt=True)
@click_config_file.configuration_option()
def add_note(author,title,message):
	""" Add A New Notes

	eg. python termipad.py add-note --author Jesse --title "Simple Terminal Notes" --message "A simple note taking cli"


	eg. python termipad.py add-note -a JCharis -t "Best Notes" -msg "This is secret"

	"""
	click.echo("==============================")
	click.secho('Author:: {}'.format(author),fg='white',bg='blue')
	click.secho('Title:: {}'.format(title),fg='white',bg='yellow')
	click.secho('Message:: {}'.format(message),fg='blue')

	click.echo("========Summary===============")
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

	click.echo(table1.table)
	click.secho('Saved Notes To DataBase',fg='blue')

@main.command()
@click.option('--title','-t',prompt=True)
def view_note(title):
	""" View Note By Title 
	
	eg.	python termipad.py view-note --title "Best Notes"

	eg.  python termipad.py view-note -t "Best Notes"

	"""
	click.secho("Searched For {}".format(title),bg='blue')
	from terminaltables import AsciiTable
	result = get_single_note(title)
	table1 = AsciiTable(result)
	click.echo(table1.table)


@main.command()
@click.argument('text')
@click.option('--by','-b',default='title')
def search(text,by):
	""" Search Note By Options [Title or Author]

	eg  termipad.py search "Jesse" --by="title"

	 """
	click.secho("Searched For :: {}".format(text),bg='blue')
	from terminaltables import AsciiTable
	if by == 'title':
		result = get_note_by_title(text)
		table1 = AsciiTable(result)
		click.echo(table1.table)
	elif by == 'author':
		result = get_note_by_author(text)
		table1 = AsciiTable(result)
		click.echo(table1.table)
	elif by == 'message':
		result = get_note_by_msg(text)
		table1 = AsciiTable(result)
		click.echo(table1.table)
	else:
		click.secho("{} Not a Choice ,Pls Try either of these [title/author/message]".format(by),bg='red')


	

@main.command()
def show_all():
	""" Show All Notes  
	
	eg. python termipad.py show-all

	"""
	click.secho("Showing All Notes",bg='blue')
	click.echo("==============================")
	from terminaltables import AsciiTable
	result = view_all_notes()
	new_result = ['Author','Title','Message']
	click.secho('{}'.format(new_result),bg='blue')
	table1 = AsciiTable(result)
	click.echo(table1.table)
	
@main.command()
@click.option('--old')
@click.option('--new')
@click.option('--field')
def edit_note(field,old,new):
	""" Edit Note By Field[title/author/message] 

	eg. python termipad.py edit-note --field="author" --old="Jesse" --new="JCharis" 

	"""
	click.secho('Editing Field:: {} with {} and Updating to {}'.format(field,old,new),fg='yellow')
	from terminaltables import AsciiTable

	click.echo("===========Previous==============")
	result2 = view_all_notes()
	new_result = ['Author','Title','Message']
	click.secho('{}'.format(new_result),bg='blue')
	table2 = AsciiTable(result2)
	click.echo(table2.table)


	if field == 'title':
		result = edit_note_title(old,new)
		table1 = AsciiTable(result)
		click.echo(table1.table)
	if field == 'author':
		result = edit_note_author(old,new)
		table1 = AsciiTable(result)
		click.echo(table1.table)
	if field == 'message':
		result = edit_note_message(old,new)
		table1 = AsciiTable(result)
		click.echo(table1.table)


	click.echo("==========Updated===============")
	result3 = view_all_notes()
	new_result2 = ['Author','Title','Message']
	click.secho('{}'.format(new_result2),bg='blue')
	table3 = AsciiTable(result3)
	click.echo(table3.table)



@main.command()
@click.option('--title')
def delete_note(title):
	""" Delete Note By Title 

	eg. python terminote.py delete-note --title "Best Notes"

	"""
	click.secho('Deleting :: {} '.format(title),fg='yellow')
	from terminaltables import AsciiTable

	click.echo("===========Previous==============")
	result2 = view_all_notes()
	new_result = ['Author','Title','Message']
	click.secho('{}'.format(new_result),bg='blue')
	table2 = AsciiTable(result2)
	click.echo(table2.table)

	result = delete_data(title)
	click.echo("Deleted From DataBase")

@main.command()
def info():
	""" Show Info About Software 
	
	eg, python termipad.py info

	"""


	click.secho('Name:: {}'.format('Termipad'),bg='red')
	click.secho('Version:: {}'.format('0.01'),bg='yellow')
	click.secho('Motto:: {}'.format('Jesus Saves@JCharisTech'),bg='green')
	click.secho('Author:: {}'.format('Jesse E Agbe(JCharis)'),bg='blue')



if __name__ == '__main__':
	main()
