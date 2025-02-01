from invoke import task
import json

from tools.app_template_maker import AppTemplate

# . $HOME/esp/esp-idf/export.fish


@task
def build(ctx, prog=False, mon=False, port=""):
    if (prog or mon) and not port:
        with open(".vscode/settings.json", "r") as file:
            settings = json.load(file)
        port = settings["idf.port"]
    cmd = "idf.py "
    if prog:
        cmd += f"--port={port} "
    cmd += "build "
    if prog:
        cmd += "flash "
    if mon:
        cmd += "monitor "
    ctx.run(cmd, pty=True)


@task
def program(ctx, mon=False, port=""):
    if not port:
        with open(".vscode/settings.json", "r") as file:
            settings = json.load(file)
        port = settings["idf.port"]
    cmd = f"idf.py --port={port} flash "
    if mon:
        cmd += "monitor "
    ctx.run(cmd, pty=True)


@task
def monitor(ctx, port=""):
    if not port:
        with open(".vscode/settings.json", "r") as file:
            settings = json.load(file)
        port = settings["idf.port"]
    cmd = "idf.py "
    cmd += f"--port={port} "
    cmd += "monitor "
    ctx.run(cmd, pty=True)


@task
def clean(ctx):
    ctx.run("idf.py fullclean")
    ctx.run("rm -rf build")
