## Objectives
* Understand {% include %},
* Understand {% block %},
* Understand the usage of each.

## Files that need to be edited

* templates in `./templates/`
    * create the child and parent templates, so it looks like the example below.
* `run.py`
    * select the right template (child or parent ?) that will be used by Jinja2.
    * for **both** outputs, give a number for the interface and a name for the policy-map.

## Example of expected outputs

```buildoutcfg
output **include** = 
! router configuration

interface Gi0/0/0.1
 no shut
 policy-map Linkt-Altitude

!! rest of the configuration



output **block** = 
! configuration


interface Gi0/0/0.1
 no shut
 policy-map Linkt-Altitude


! end of configuration

Process finished with exit code 0

```