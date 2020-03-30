# task.py
#
#
# Dennis Wai 3/29/2020

from invoke import Collection, task
import cmd
from colorama import Fore, Style


@task()
def build(c):
    '''
    Perform a one time build of the Jekyll source
    '''
    print(Fore.GREEN +
          "Doing one time build of Jekyll site..." +
          Style.RESET_ALL)
    cmd.jekyll.build(c)


@task()
def serve(c):
    '''
    Serves website locally for development
    '''
    print(Fore.GREEN +
          "Running Jekyll as a service..." +
          Style.RESET_ALL)
    cmd.jekyll.serve(c)


# Add all the top level tasks to the namespace
ns = Collection()
ns.add_task(build)
ns.add_task(serve)
