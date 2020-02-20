import jinja2

# Where's the folder with my templates (or my folders, if multiple)
template_loader = jinja2.FileSystemLoader(searchpath="./templates")

# Instance of the Environment class. Gives the loader (above), optionally parameters like
# block strings, variable strings etc.
template_env = jinja2.Environment(loader=template_loader)

# Which file is my template
# EXERCISE : select the right template (child or parent ?) that will be used by Jinja2.
template_include = template_env.get_template("EXERCISE")
template_block = template_env.get_template("EXERCISE")

# EXERCISE for **both** outputs, give a number for the interface and a name for the policy-map.
# Output for include
print("output **include** = \n{output}".format(output=template_include.render(EXERCISE)))

print("\n\n")
# Output for block
print("output **block** = \n{output}".format(output=template_block.render(EXERCISE)))