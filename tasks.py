from invoke import task # type: ignore

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage html")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")
