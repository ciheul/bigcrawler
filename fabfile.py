import os
from contextlib import contextmanager
from fabric.api import *
from fabric.contrib.files import exists


env.hosts = ['winnuayi@192.168.1.2']
env.password = 'liverpool'
env.colorize_errors = True

PROJECTS_DEV_DIR = '~/Projects/dev'
BACKEND_DIR = os.path.join(PROJECTS_DEV_DIR, 'backend')
BIGCRAWLER_DIR = os.path.join(BACKEND_DIR, 'bigcrawler')
VENV_DIR = os.path.join(PROJECTS_DEV_DIR, 'virtualenv')
VENV_BIGCRAWLER_DIR = os.path.join(VENV_DIR, 'bigcrawler')

GIT_BIGCRAWLER = 'https://github.com/ciheul/bigcrawler'


def setup():
    sudo("apt-get install libxml2-dev")
    sudo("apt-get install libxslt1-dev")
    sudo("apt-get install python-dev")
    sudo("touch /data/db")
    sudo("apt-get install mongodb-server")
    sudo("pip install virtualenv")

    # TODO install MongoDB
    # TODO run MongoDB


def update_crawler():
    """Update to the latest version."""
    with cd(BIGCRAWLER_DIR):
        run('git pull')


def deploy():
    """Setup a new server for the first time."""
    setup()

    ## create dev folder 
    #if not exists(PROJECTS_DEV_DIR):
    #    run("mkdir -p " + PROJECTS_DEV_DIR)

    if not exists(VENV_BIGCRAWLER_DIR):
        run("mkdir -p " + VENV_DIR)
        with cd(VENV_DIR):
            run("virtualenv bigcrawler")

    # for the first time, git clone. otherwise, ignore
    if not exists(BIGCRAWLER_DIR):
        run("mkdir -p " + BACKEND_DIR)
        with cd(BACKEND_DIR):
            run('git clone ' + GIT_BIGCRAWLER)

    with prefix("source " + os.path.join(VENV_BIGCRAWLER_DIR, 'bin/activate')):
        with cd(BIGCRAWLER_DIR):
            run("pip install -r requirements.txt")


def clean():
    """Remove anything related to BigCrawler."""
    with cd(BACKEND_DIR):
        run("rm -rf bigcrawler")

    with cd(VENV_DIR):
        run("rm -rf bigcrawler")
