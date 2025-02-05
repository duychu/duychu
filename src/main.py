"""
Module to create README for Github Profile.
"""

import io
from datetime import datetime
from jinja2 import Template


def create_readme():
    """
    Creates the Readme.md from the Readme template.
    """

    readme = io.open('../readme.md', 'w+', encoding='utf-8')
    template = Template(io.open('readme.template.md', 'r', encoding='utf-8').read())
    readme_data = template.render(
        last_updated=get_last_updated())
    readme.write(readme_data)
    readme.close()


def get_last_updated():
    """
    Returns the last updated date.
    """

    now = datetime.now()
    return datetime.strftime(now, '%d %b, %Y')


def main():
    """
    Main function for the Module.
    """
    create_readme()


if __name__ == '__main__':
    main()
