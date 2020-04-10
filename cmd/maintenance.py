# maintenance.py
#
# Namespace of less commonly used tasks
#
# Dennis Wai 3/29/2020

from invoke import Collection, task
from colorama import Fore, Style


@task
def htmlproof(c):
    '''
    Runs html proofer over built site
    '''
    print(Fore.GREEN +
          "Running HTMLProofer..." +
          Style.RESET_ALL)
    c.run("docker run -v $PWD/src/_site/:/mounted-site 18fgsa/html-proofer /mounted-site")
