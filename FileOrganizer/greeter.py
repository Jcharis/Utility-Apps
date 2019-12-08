import click
import click_config_file


@click.group()
@click.version_option(version='0.01',prog_name='greeter')
def main():
	""" Greeter : greeting in diverse languages
	"""
	pass


@main.command()
@click.argument('name')
@click.option('--time','-t',help='Specify Time of Day to Greet',default='am')
@click_config_file.configuration_option()
def greet(name,time):
	click.echo('Hello {},good {}'.format(name,time))





if __name__ == '__main__':
	main()