import os
import string 

class Github:
    def __init__(self):
        readme_template = os.path.join('Data\\README_Template','readme-template.txt')
        custom_template = []
        with open(readme_template,'r') as f:
            mytemplate = f.read()
            custom_template.append(mytemplate)
        self.temp = custom_template
    
    def license_choices(self):
        filename = [f.split('.')[0] for f in os.listdir('Data\\LICENSE_Template')]
        return filename

    def load_license(self,filename):
        license_template = os.path.join('Data\\LICENSE_Template',f'{filename}.txt')
        custom_license = []
        with open(license_template,'r') as f:
            mytemplate = f.read()
            custom_license.append(mytemplate)
            return custom_license
        
    def write_license(self,license_temp,projectname):
        for lines in license_temp:
            license_placeholders = [placeholder[1] for placeholder in string.Formatter().parse(lines) if placeholder[1]]
            license_inputs = {placeholder: input(f'Enter a {placeholder}: ') for placeholder in license_placeholders}
            custom_license_filled = lines.format(**license_inputs)
            with open(os.path.join(projectname,'License.md'),'w') as f:
                f.write(custom_license_filled)

    def fill_template(self,github_username,repository):
        custom_template = self.temp
        template = self.temp[0]
        my_license_choices = self.license_choices()
        all_acknowledgements = []

        for line in custom_template:
            placeholders = [placeholder[1] for placeholder in string.Formatter().parse(line) if placeholder[1]]
            try:
                user_inputs = {}
                print()
                for placeholder in placeholders:
                    if placeholder == 'License':
                        print('Enter a License')
                        print('----------------')
                        for i, license in enumerate(my_license_choices):
                            print(f'{i+1}. {license}')
                        choice = int(input('Enter the number associated with your license choice: '))
                        if isinstance(choice,int):
                            user_inputs[placeholder] = my_license_choices[choice-1]
                    elif placeholder == 'Github Username':
                        user_inputs[placeholder] = github_username
                    elif placeholder == 'Repo Name':
                        user_inputs[placeholder] = repository
                    elif placeholder == 'Github Name':
                        user_inputs[placeholder] = github_username.capitalize()
                    elif placeholder == 'Inspiration RepoName':
                        acknowledgements = int(input('How many shout outs would you like to give: '))                
                        if isinstance(acknowledgements,int):
                            all_acknowledgements.append(acknowledgements)
                        if all_acknowledgements[0] == 1: 
                            user_inputs[f'Inspiration RepoName'] = input(f'Enter a Inspiration RepoName: ')
                            user_inputs[f'Inspiration Repo link'] = input(f'Enter a Inspiration Repo link: ') 
                
                        elif all_acknowledgements[0] >= 2 :
                            template = self.temp[0].replace("* [{Inspiration RepoName}]", "").replace("({Inspiration Repo link})", "")
                            for i in range(all_acknowledgements[0]):
                                user_inputs[f'Inspiration RepoName{i+1}'] = input(f'Enter a Inspiration RepoName{i+1}: ')
                                user_inputs[f'Inspiration Repo link{i+1}'] = input(f'Enter a Inspiration Repo link{i+1}: ')
                                template += "* [" + "{Inspiration RepoName" + str(i+1) + "}]"+ "({Inspiration Repo link" +str(i+1)+"})\n"

                    elif placeholder == 'Inspiration Repo link' :
                        pass
                    else:
                        user_inputs[placeholder] = input(f'Enter a {placeholder}: ')
            except KeyboardInterrupt:
                exit(0)

            #print(user_inputs)
            print(template)

            projectname = user_inputs['Project Title']
            if not os.path.exists(projectname):
                os.mkdir(projectname)
            
            license_temp = self.load_license(user_inputs['License'])
            self.write_license(license_temp,projectname)
   
            custom_temp_filled = template.format(**user_inputs)
        
            with open(os.path.join(projectname,'README.md'),'w') as f:
                f.write(custom_temp_filled)
                    