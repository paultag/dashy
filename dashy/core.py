import os
import github3


def load_key():
    with open(os.path.expanduser("~/.dashy.key"), 'r') as fd:
        key = fd.read().strip()
    return key


github = github3.GitHub("paultag", load_key())
