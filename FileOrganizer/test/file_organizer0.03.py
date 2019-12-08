#!/usr/bin/python
# -*- coding: UTF-8 -*-

import click
import os
import fnmatch
import shutil

# File Sorting and Organization
def organize_files_by_keyword(keyword):
    for file in os.listdir("."):
        # If the name of the file contains a keyword
        if fnmatch.fnmatch(file,'*' + keyword + '*'):
            print("Found:",file)
            # If the file is truly a file...
            if os.path.isfile(file):
                try:
                    # Make a directory with the keyword name...
                    os.makedirs(keyword)
                except:
                    None
                # Move that file to the directory with that keyword name
                print("Moving File:",file)
                shutil.move(file,keyword)


@click.group()
@click.version_option(version='0.02',prog_name='file_organizer')
def main():
	""" File Organizer is a simple tool to organize and sort files into folders

	eg. file_organizer.py  organize .
	"""
	pass


@main.command()
@click.argument('current_path')
@click.option('--keyword','-k',help="Specify Keyword to Search Default is YYYYY",default='YYYY')
def organize(current_path,keyword):
	""" Organize Files and Sort Them Into Folders By Keyword

		eg. file_organizer organize .

		eg. python file_organizer.py organize .

		eg. python file_organizer.py organize . --keyword YYYY

		eg. python file_organizer.py organize . --keyword myfolder
		
		eg. python file_organizer.py organize 
		
	"""
	if keyword == 'YYYY':
		try:
		    year_regex = re.compile(r'\d{4}') # Regex to Find First 4 yyyyy in a list
		    all_keywords = []

		    for file in os.listdir(current_path):
		    	# found_result = year_regex.search(file).group()
		    	found_result = year_regex.findall(file)[0]
		    	all_keywords.append(found_result)
		    	final_keywords = list(set(all_keywords))

		    	for word in final_keywords:
		    		click.secho(('Found File::{}'.format(file)),fg='blue')
		    		organize_files_by_keyword(word)
		    		click.secho(('Finished Moving to:{}'.format(word)),fg='green')
		except IndexError:
		    pass
	else:
		click.secho(('Organizing By Keyword :{}'.format(keyword)),fg='green')
		organize_files_by_keyword(keyword.lower())
		click.secho(('Finished Moving to:{}'.format(keyword)),fg='green')



@main.command()
@click.argument('current_path')
@click.option('--extension','-e',help="Specify Extension to Sort By: Default is .txt",default='txt')
def organize_by_ext(current_path,extension):
	""" Organize Files and Sort Them Into Folders By Extension

		eg. file_organizer organize-by-ext .

		eg. python file_organizer.py organize-by-ext .

		eg. python file_organizer.py organize-by-ext . --extension txt

		eg. python file_organizer.py organize-by-ext  . --extension .csv
		
	"""
	for file in os.listdir(current_path):
		ext = extension
		if fnmatch.fnmatch(file,'*' + ext):
		    click.secho(('Found File:{}'.format(file)),fg='blue')
		    # If the file is truly a file...
		    if os.path.isfile(file):
		        try:
		            # Make a directory with the extension name...
		            new_dir = ext.strip(".")
		            os.makedirs(new_dir)
		        except:
		            None
		        # Copy that file to the directory with that extension name
		        shutil.move(file,new_dir)
	click.secho(('Finished Moving {} to:{} folder'.format(file,new_dir)),fg='green')


@main.command()
@click.argument('current_path')
def organize_by_order(current_path):
	""" Organize Files and Sort Them Into Folders Alphabetical and Numerically

		eg. file_organizer organize-by-order .

		eg. python file_organizer.py organize-by-order .

		eg. python file_organizer.py organize-by-order . 

		
	"""
	for file in sorted(os.listdir(current_path)):
		if file != 'file_organizer.py':
			try:
				os.makedirs(file[0])
				click.echo("Creating a Folder",file[0])
			except:
				None
			shutil.move(file,file[0])
			click.secho(('Finished moving : {} to {} folder'.format(file,file[0])),fg='green')


@main.command()
@click.argument('current_path')
@click.option('casetype','-c',help='Case Type [lower,upper,title]',default='lower')
def bulk_rename(current_path,casetype):
	""" Rename Multiple Files with a Case Type[lower,upper,title]

		eg. file_organizer bulk-rename .

		eg. python file_organizer.py bulk-rename . --casetype upper

		eg. python file_organizer.py bulk-rename . -c lower

		
	"""
	click.echo(current_path)
	filenames = os.listdir(current_path) 

	for filename in filenames:
		if filename != 'file_organizer0.03.py':
			if casetype == 'lower':
				click.secho('Renaming ::> {} to same name in {} case'.format(filename,casetype),fg='green')
				click.echo(filename.lower())
				os.rename(filename,filename.replace(" ","-").lower())
			elif casetype == 'upper':
				click.secho('Renaming ::> {} to same name in {} case'.format(filename,casetype),fg='green')
				click.echo(filename.upper())
				os.rename(filename,filename.replace(" ","-").upper())
				
			elif casetype == 'title':
				click.secho('Renaming ::> {} to same name in {} case'.format(filename,casetype),fg='green')
				click.echo(filename.title)
				os.rename(filename,filename.replace(" ","-").title())
				
			else:
				click.secho('Renaming ::> {} to same name in {} case'.format(filename,casetype),fg='green')
				click.echo(filename.lower())
				os.rename(filename,filename.replace(" ","-").lower())

	click.secho('Finished Renaming to {} case!!'.format(casetype),bg='blue',fg='white')
if __name__ == '__main__':
	main()
	