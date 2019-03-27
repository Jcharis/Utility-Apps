#!/usr/bin/python


import click
import os,shutil
import fnmatch

def organize_files_by_keyword(keyword):
	for file in os.listdir("."):
		if fnmatch.fnmatch(file,"*"+keyword+"*"):
			print("Found",file)
			# If the file is truly a file
			if os.path.isfile(file):
				try:
					os.makedirs(keyword)
				except:
					None
				print("Moving File",file)
				shutil.move(file,keyword)



@click.group()
@click.version_option(version='0.01',prog_name='file_organizer')
def main():
	""" File Organizer: a simple tool to organize and sort files into folders

	"""
	pass

@main.command()
@click.argument('current_path')
@click.option('--keyword','-k',help='Specify the Keyword to sort by')
def organize(current_path,keyword):
	""" Organize by Keyword

	eg. python file_organizer organize . --keyword newscript

	"""

	click.secho(('Organizing by keyword: {}'.format(keyword)),fg='blue')
	organize_files_by_keyword(keyword.lower())
	click.secho(('Finished moving to: {}'.format(keyword)),fg='green')


@main.command()
@click.argument('current_path')
@click.option('--extension','-e',help='Specify the Extension to sort by')
def organize_by_ext(current_path,extension):
	""" Organize by extension

	eg file_organizer organize-by-ext . --extension csv

	"""
	for file in os.listdir(current_path):
		ext = extension
		if fnmatch.fnmatch(file,"*"+ ext):
			click.secho(('Found File:{}'.format(file)),fg='blue')
			# If the file is truly a file
			if os.path.isfile(file):
				try:
					new_dir = ext.strip(".")
					os.makedirs(new_dir)
				except:
					None
				print("Moving File",file)
				shutil.move(file,new_dir)
			click.secho(('Finished moving {} to: {}'.format(file,new_dir)),fg='green')




if __name__ == '__main__':
	main()
