## Objectives
* import variables from a yaml file,
* storing the output in a file.

## Files that need to be edited

* `variables.yaml`
    * this file is where you are going to store the variables.
        * `name` of the policy
        * `number` of the interface
* `run.py`
    * open the `.yaml` file to read its content. You will also use this function to write in the `output` file.
        * https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    * use the `yaml` library in order to convert the `.yaml` in a dictionary.
        * https://pyyaml.org/wiki/PyYAMLDocumentation
        * Look at `safe_load(stream)`
    * pass the variable to Jinja2 as a dictionary.
* `template.tpl` in `./templates/`
    * in `run.py`, you will pass a dictionary to Jinja. Create the template file as such. 
* `output.txt` in `./output/`
    * make sure this output file exists. The configuration will be added in this file.

## Example of expected outputs

```buildoutcfg
output =
 interface Gi0/0/0.1
 no shut
 policy-map Linkt-Altitude
```