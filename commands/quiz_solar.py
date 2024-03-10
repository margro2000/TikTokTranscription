import os
BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
import sys
sys.path.append(BASE_DIR)

from utils.solar_helpers import quiz_solar_about_module
import asyncclick as click


@click.command()
@click.argument('module_title')
@click.argument('question')
def cmd_quiz_solar(module_title, question):
    """"""
    answer = quiz_solar_about_module(module_title, question)

    print(answer)


if __name__ == '__main__':
    cmd_quiz_solar()
