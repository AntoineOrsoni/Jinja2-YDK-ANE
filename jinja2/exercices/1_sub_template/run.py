import jinja2

# Where's the folder with my templates (or my folders, if multiple)
template_loader = jinja2.FileSystemLoader(searchpath="./templates")

# Instance of the Environment class. Gives the loader (above), optionally parameters like
# block strings, variable strings etc.
template_env = jinja2.Environment(loader=template_loader)

# Which file is my template
template_include = template_env.get_template("parent_template_include.tpl")
template_block = template_env.get_template("block/child_template_block.tpl")

# Output for include
print("output **include** = \n{output}".format(output=template_include.render(number=1, name="Linkt-Altitude")))

print("\n\n")
# Output for block
print("output **block** = \n{output}".format(output=template_block.render(number=1, name="Linkt-Altitude")))
