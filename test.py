from Github_Blueprints.Blueprints import Github

github_username = 'example name' #change to your username
repository = 'example repo' #change to the name of the repo

create = Github()
create.fill_template(github_username,repository)