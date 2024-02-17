import string
import os

def load_template():
    template = os.path.join('README_Template','readme-template.txt')
    custom_template = []
    with open(template,'r') as f:
        mytemplate = f.read()
        custom_template.append(mytemplate)
        return custom_template
    
def license_choices():
    filename = [f.split('.')[0] for f in os.listdir('LICENSE_Template')]
    return filename

def load_license(filename):
    license_template = os.path.join('LICENSE_Template',f'{filename}.txt')
    custom_license = []
    with open(license_template,'r') as f:
        mytemplate = f.read()
        custom_license.append(mytemplate)
        return custom_license

def fill_template(custom_template):

    for line in custom_template:
        placeholders = [placeholder[1] for placeholder in string.Formatter().parse(line) if placeholder[1]]
        user_inputs = {placeholder: input(f'Enter a {placeholder}: ') for placeholder in placeholders}

        if 'License' in user_inputs and user_inputs['License'] in license_choices():
            license_temp = load_license(user_inputs['License'])
            for lines in license_temp:
                license_placeholders = [placeholder[1] for placeholder in string.Formatter().parse(lines) if placeholder[1]]
                license_inputs = {placeholder: input(f'Enter a {placeholder}: ') for placeholder in license_placeholders}
                custom_license_filled = lines.format(**license_inputs)
                with open('License.md','w') as f:
                    f.write(custom_license_filled)

        custom_temp_filled = line.format(**user_inputs)
        with open('README.md','w') as f:
            f.write(custom_temp_filled)

custom_template = load_template()
fill_template(custom_template)