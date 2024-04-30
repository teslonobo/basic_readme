from sys import argv
from Github_Blueprints.Blueprints import Github


github_username = argv[1]
repository = argv[2]

create = Github().fill_template(github_username,repository)