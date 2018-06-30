from invoke import task
import os


@task
def lint(c):
    os.system("flake8 .")
    # os.system("yapf --style pep8 -i showjar.py")


@task
def test(c):
    os.system("nosetests")


@task
def commit(c):
    os.system("git add -A && git commit")


@task
def push(c):
    os.system("git push")


@task
def deploy(c):
    lint(c)
    test(c)
    commit(c)
    push(c)
