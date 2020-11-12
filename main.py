from pathlib import Path

import click


class Config:
    def __init__(self):
        pass


pass_config = click.make_pass_decorator(
    Config,  # Class whose instance will be passed around
    ensure=True  # causes an instance to be created upon first usage
)


@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--data-dir', type=click.Path(), default=Path('.'))
@pass_config  # creates an empty Config object
def entrypoint_fn(config, verbose, data_dir):
    """Main entrypoint of our app"""
    config.verbose = verbose
    config.data_dir = data_dir


@entrypoint_fn.command()
@click.option('--opt1', type=int, default=42, help='option 1')
@click.option('--opt2', type=float, required=False, help='option 2')
@click.argument('outf', type=click.File('w'), default='-')
@pass_config
def subcommand(config, opt1, opt2, outf):
    """subcommand with additional options"""
    if config.verbose:
        click.echo('VERBOSE MODE')
    click.echo(f'Data dir is: {config.data_dir}')
    click.echo(f'Option 1: {opt1}', file=outf)
    click.echo(f'Option 2: {opt2}', file=outf)
