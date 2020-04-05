# jekyll.py
#
#
# Dennis Wai 3/29/2020

from invoke import task
JEKYLL_SRC_DIR = "src/"


@task()
def serve(c):
    '''
    Runs jekyll serve via Docker
    '''
    with c.cd(JEKYLL_SRC_DIR):
        cmd = "docker run --rm --name spam \
              --volume=\"$PWD:/srv/jekyll\" \
              --volume=\"$PWD/vendor/bundle:/usr/local/bundle\" \
              -p 4000:4000  -it jekyll/jekyll:3.8 \
              jekyll serve --force_polling"
        c.run(cmd, pty=True)


@task()
def build(c):
    '''
    Perform a one time build of the Jekyll source.
    '''
    with c.cd(JEKYLL_SRC_DIR):
        cmd = "docker run --rm --volume=\"$PWD:/srv/jekyll\" \
              --volume=\"$PWD/vendor/bundle:/usr/local/bundle\" -it \
              jekyll/jekyll:3.8 jekyll build"
        c.run(cmd, pty=True)


@task
def bundle(c):
    '''
    Runs jekyll bundle to reinstall all the ruby gems
    '''
    with c.cd(JEKYLL_SRC_DIR):
        c.run("docker run --rm --volume=\"$PWD:/srv/jekyll\" \
              --volume=\"$PWD/vendor/bundle:/usr/local/bundle\" \
              -it jekyll/jekyll:3.8 bundle install", pty=True)


@task
def profile(c):
    '''
    Creates a report on what parts of site takes the longest to build
    '''
    with c.cd(JEKYLL_SRC_DIR):
        c.run("docker run --rm --volume=\"$PWD:/srv/jekyll\" \
              --volume=\"$PWD/vendor/bundle:/usr/local/bundle\" \
              -it jekyll/jekyll:3.8 jekyll build --profile", pty=True)
