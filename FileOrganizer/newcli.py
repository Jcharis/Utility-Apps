import click
import click_config_file

@click.command()
@click.option('--name', default='World', help='Who to greet.')
@click.option('--age')
@click_config_file.configuration_option()
def hello(name,age):
    click.echo('Hello {} {}!'.format(name,age))



if __name__ == '__main__':
	hello()