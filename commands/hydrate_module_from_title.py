
import asyncclick as click

import os

import sys
BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(BASE_DIR)
from App import hydrate_module_from_title

@click.command()
@click.argument('module_title')
@click.option('--save/--no-save', default=False)
def cmd_hydrate_module_from_title(module_title, save):
    """"""
    print(module_title)
    result = hydrate_module_from_title(module_title, save)

    print(result)


if __name__ == '__main__':
    cmd_hydrate_module_from_title()
