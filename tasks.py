from invoke import task, Context


@task(help={"file": "Path to input file."})
def start(ctx: Context, file: str) -> None:
    """
    Run the program with path of input file as argument.
    """
    ctx.run(f"python3 src/index.py --file {file}", pty=True)
