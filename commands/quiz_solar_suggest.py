import os
BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
import sys
sys.path.append(BASE_DIR)

from App import quiz_solar_about_module, generate_module_suggestions
from pprint import pprint
import asyncclick as click


@click.command()
@click.argument('module_title')
@click.argument('question')
def cmd_quiz_solar(module_title, question):
    """"""
    answer = quiz_solar_about_module(module_title, question)

    print(answer)
    
    suggestions = generate_module_suggestions(module_title, question, answer)

    pprint(suggestions)


if __name__ == '__main__':
    cmd_quiz_solar()
