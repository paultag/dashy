from dashy.prs import get_prs

def print_pr(pr):
    _, name = pr.repository
    print("{name}[20G{pr.number}[27G{pr.assignee}[40G{pr.title}[0m".format(
        pr=pr, name=name
    ))

for pr in get_prs([
    ("sunlightlabs", "openstates"),
    ("opencivicdata", "pupa"),
    ("opencivicdata", "scrapers-municipal-us"),
]):
    print_pr(pr)
