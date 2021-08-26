import subprocess
import shlex


def process_tasks():
    process_tasks_cmd = "python manage.py process_tasks --duration 60"
    process_tasks_args = shlex.split(process_tasks_cmd)
    process_tasks_subprocess = subprocess.Popen(process_tasks_args)
