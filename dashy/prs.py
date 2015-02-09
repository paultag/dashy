from .core import github


def get_pr(user, repo):
    repo = github.repository(user, repo)
    requests = repo.pull_requests()
    for request in requests:
        yield request


def get_prs(repos):
    for repo in repos:
        yield from get_pr(*repo)
