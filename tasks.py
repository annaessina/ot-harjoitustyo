from invoke import task


@task
def start(ctx):
    ctx.run("python3 calculator/src/index.py", pty= True)

@task
def test(ctx):
    ctx.run("pytest calculator/src", pty= True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive calculator/src", pty=True)

@task
def build(ctx):
    ctx.run("python3 calculator/src/build.py", pty=True)

@task
def lint(ctx):
    ctx.run("pylint calculator/src", pty=True)
