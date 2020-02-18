import jinja2
import yaml

# Where's the folder with my templates (or my folders, if multiple)
template_loader = jinja2.FileSystemLoader(searchpath="./templates")

# Instance of the Environment class. Gives the loader (above), optionally parameters like
# block strings, variable strings etc.
template_env = jinja2.Environment(loader=template_loader)

# Which file is my template
template = template_env.get_template("template.tpl")

# Loading my variables, stored in a YAML file
with open("variables.yaml", 'r') as variables_file:
    variables = yaml.safe_load(variables_file)

    outputText = ""
    # Generating the output for BundleEthernet interfaces
    outputText += template.render(variables=variables)

print("output =\n {output}".format(output=outputText))

# Saving the output in a text file
# Content of the file gets removed every time. Then content is added.
with open("./output/output.txt", "w") as output_file:
    print(outputText, file=output_file)