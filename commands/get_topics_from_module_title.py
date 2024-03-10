
import asyncclick as click

import os

import sys
BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(BASE_DIR)

from App import generate_topics_from_module_title


@click.command()
@click.argument('module_title')
async def create_topics_from_module_title(module_title):
    """"""
    print(module_title)
    result = generate_topics_from_module_title(module_title)

    print(result)

if __name__ == '__main__':
    create_topics_from_module_title(_anyio_backend="asyncio")
