from __future__ import with_statement
import subprocess
import tempfile

def make_directory(path):
    subprocess.check_call(['mkdir', '-p', path])

def remove_directory(path):
    subprocess.check_call(['rm', '-rf', path])

def git_init(path):
    subprocess.check_call(['git', '--bare', 'init', path])

def link(source, target):
    subprocess.check_call(['ln', '-sr', source, target])

def unlink(source, target):
    subprocess.check_call(['find', target,  '-follow', '-samefile', source, '-exec', 'rm', '-f', '{}', '+'])

def fingerprint(key):
    with tempfile.NamedTemporaryFile() as f:
        f.write(key + '\n')
        f.flush()
        bit, fingerprint, description = subprocess.check_output(['ssh-keygen', '-lf', f.name]).split(None, 2)
        return fingerprint

