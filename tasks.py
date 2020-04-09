# task.py
#
#
# Dennis Wai 3/29/2020

from invoke import Collection, task
import cmd
from colorama import Fore, Style
from datetime import datetime
import sys


@task()
def build(c):
    '''
    Perform a one time build of the Jekyll source
    '''
    print(Fore.GREEN +
          "Doing one time build of Jekyll site..." +
          Style.RESET_ALL)
    cmd.jekyll.build(c)


def push_to_server(c, msg, branch):
    '''
    Creates a commit and then push to master w/ error handling
    '''
    c.run("git add -u")
    res = c.run('git commit -m "%s"' % msg)
    res = c.run("git push origin %s" % branch)
    if res.exit_code() != 0:
        print(Fore.RED +
              "Unable to deploy site to %s" % branch +
              Style.RESET_ALL)
        print(res.stdout)
        print(res.stderr)
        sys.exit(1)


@task()
def deploy(c):
    '''
    Copies current Jekyll src and puts in submodule and git push
    '''
    print(Fore.GREEN +
          "Deploying site..." +
          Style.RESET_ALL)
    # Figure out if there are uncommitted changes in src before proceeding
    res = c.run("git status --porcelain | grep -v site", hide=True, warn=True)
    if res and len(res.stdout) > 0:
        # Implies that there are uncommitted changes
        print(Fore.RED +
              "You have uncommitted changes\n" +
              "Address them before deploying." +
              Style.RESET_ALL)
        sys.exit(1)

    cmt_msg = "Deployed site on " + datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    c.run("cp -r src/* site/")
    with c.cd("site"):
        push_to_server(c, cmt_msg, "master")
    # This will add the update to the submodule and commit it as well
    push_to_server(c, cmt_msg, "master-src")


@task()
def serve(c):
    '''
    Serves website locally for development
    '''
    print(Fore.GREEN +
          "Running Jekyll as a service..." +
          Style.RESET_ALL)
    cmd.jekyll.serve(c)


@task()
def prereqs(c):
    '''
    Installs all the gems
    '''
    print(Fore.GREEN +
          "Installing gems..." +
          Style.RESET_ALL)
    cmd.jekyll.bundle(c)


# Add all the top level tasks to the namespace
ns = Collection()
ns.add_task(build)
ns.add_task(serve)
ns.add_task(prereqs)
ns.add_task(deploy)
