import sys
import click

@click.group()
@click.version_option("0.1.0")
def main():
    """My Journal CLI"""
    print("My Journal CLI")
    pass

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("This is help")
    main()