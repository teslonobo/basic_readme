from Github_Blueprints.Blueprints import Github

github_username = 'teslonobo'
repository = 'readme_basic'

create = Github()
create.fill_template(github_username,repository)