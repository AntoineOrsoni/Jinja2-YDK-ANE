## Objectives
* Use conditions (if, else),
* Use loops (for),
* Combine the two together,
* Whitespace control.

## Files that need to be edited

* `template.tpl` in `./templates/`
    * create the template file, and the logic so it looks like the output below.
    * create a loop to create 10 interfaces
    * create a condition
        * if interface_number is even policy_name = XXX
        * elif interface_number is odd policy_name = YYY
    * use whitespace control to have the same indentation and spacing as the output below.
* `run.py`
    * pass a name for policy_name_odd and another for policy_name_even.
    * you don't need to pass a policy_number as it will be given inside the loop, in the template file.
    
## Example of expected outputs

```buildoutcfg
output **include** = 

interface Gi0/0/0.0
 no shut
 policy-map Linkt

interface Gi0/0/0.1
 no shut
 policy-map Altitude

interface Gi0/0/0.2
 no shut
 policy-map Linkt

interface Gi0/0/0.3
 no shut
 policy-map Altitude

interface Gi0/0/0.4
 no shut
 policy-map Linkt

interface Gi0/0/0.5
 no shut
 policy-map Altitude

interface Gi0/0/0.6
 no shut
 policy-map Linkt

interface Gi0/0/0.7
 no shut
 policy-map Altitude

interface Gi0/0/0.8
 no shut
 policy-map Linkt

interface Gi0/0/0.9
 no shut
 policy-map Altitude
```