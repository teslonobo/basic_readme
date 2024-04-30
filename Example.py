from Github_Blueprints.Blueprints import Github

github_username = 'Example' #change to your username
repository = 'Example' #change to the name of the repo

# Create a Github object
create = Github() 
# Now lets fill it
create.fill_template(github_username,repository)