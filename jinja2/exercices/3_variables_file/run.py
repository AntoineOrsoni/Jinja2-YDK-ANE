import jinja2
import yaml

# Where's the folder with my templates (or my folders, if multiple)
template_loader = jinja2.FileSystemLoader(searchpath="./templates")

# Instance of the Environment class. Gives the loader (above), optionally parameters like
# block strings, variable strings etc.
template_env = jinja2.Environment(loader=template_loader)

# Which file is my template
template = template_env.get_template("template.tpl")

# EXERCISE : Open the .yaml file. Load the variables, stored in a YAML file.

# EXERCISE : Construct your output with the render() method.

# EXERCISE : Saving the output in a text file. Open the `output.txt` file, and write your output inside.
