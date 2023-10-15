from invoke import task


@task
def generoi(ctx):
    ctx.run("python3 src/main.py", pty=True)


@task
def testaa(ctx):
    ctx.run("pytest src", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
