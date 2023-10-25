from invoke import task


@task
def testaa(ctx):
    ctx.run("pytest src", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
