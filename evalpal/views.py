import functools
import subprocess
import tempfile

from evalpal import app
from sanic.response import json


def safely_run_subprocess(unsafe_command, code):
    with tempfile.NamedTemporaryFile() as temp:
        temp.write(code)
        temp.flush()
        command = 'firejail --noprofile --force --quiet {} {}'.format(unsafe_command, temp.name)
        completed = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    return completed


@app.route("/node", methods=["POST"])
async def evaluate_node(request):
    safely_run_node = functools.partial(safely_run_subprocess, 'node')
    completed_process = safely_run_node(request.body)
    return json(completed_process.stdout)


@app.route("/ruby", methods=["POST"])
async def evaluate_ruby(request):
    safely_run_ruby = functools.partial(safely_run_subprocess, 'ruby')
    completed_process = safely_run_ruby(request.body)
    return json(completed_process.stdout)


@app.route("/python", methods=["POST"])
async def evaluate_python(request):
    safely_run_python = functools.partial(safely_run_subprocess, 'python')
    completed_process = safely_run_python(request.body)
    return json(completed_process.stdout)


@app.route("/elixir", methods=["POST"])
async def evaluate_elixir(request):
    safely_run_elixir = functools.partial(safely_run_subprocess, 'iex')
    completed_process = safely_run_elixir(request.body)
    return json(completed_process.stdout)
