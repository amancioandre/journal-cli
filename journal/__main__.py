import os
import sys
import click
import yaml
import subprocess

from yaml import CLoader as Loader
from datetime import datetime

from journal.templates.entries import week_entry


@click.group()
@click.version_option("0.1.0")
def main():
    """Simple Journal CLI"""
    pass

@main.command()
@click.argument('name', required=False)
@click.option('--no-conf', help="Pass this option if you want to create a new Journal without any configuration")
def new(**kwargs):
    """Creates a new journal with the name provided"""
    name = None
    if not kwargs.get("name"):
        while (not name):
            name = click.prompt("Please enter a valid name", type=str)
    else:
        name = kwargs.get("name")

    if kwargs.get("--no-conf"):
        os.mkdir(name)
        return

    config = {
    'author': None,
    }

    while (not config.get('author')):
        config['author'] = click.prompt("Please enter an author name", type=str)

    os.mkdir(name)
    os.chdir(name)

    with open("config.yaml", "w") as config_file:
        config_file.write(yaml.dump(config))

@main.command()
def create(**kwargs):
    """Creates, or opens, a journal entry for the current year and week with the default editor"""
    try:
        config_file = open("config.yaml", "r").read()
    except FileNotFoundError as _:
        print("Configuration file not found")
        return
    config = yaml.load(config_file, Loader=Loader)
    
    today = datetime.today()
    iso_date = today.isocalendar()
    year = iso_date.year
    week = iso_date.week

    entry = week_entry(date=today.isoformat(), year=year, week=week, author=config.get("author"))
    dir_path = f"{year}/weeks/"
    file_name = f"{year}W{week}.md"

    try:
        os.chdir(dir_path)
    except Exception as _:
        os.makedirs(dir_path)
        os.chdir(dir_path)

    with open(file_name, "w") as week_entry_file:
        week_entry_file.write(entry)
        subprocess.call(['code', file_name])

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("This is help")
    main()