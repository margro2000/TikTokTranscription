import asyncclick as click

import os

from celery import Task

from api.celery import celery

import sys
import uuid

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(BASE_DIR)
from App import hydrate_module_from_title


@click.command()
@click.argument("module_title")
@click.option("--save/--no-save", default=False)
def cmd_hydrate_module_from_title(module_title, save):
    """"""
    print(module_title)
    result = hydrate_module_from_title(module_title, save)

    print(result)


@celery.task
def task_hydrate_module_from_title(**kwargs) -> Task:
    """"""
    module_title = kwargs.get("module_title")
    save = kwargs.get("save", False)

    course_id = str(uuid.uuid4())

    print(module_title)
    result = hydrate_module_from_title(module_title, course_id, save)

    print(result)


if __name__ == "__main__":
    cmd_hydrate_module_from_title()
