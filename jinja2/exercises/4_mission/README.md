## Objectives

* Re-use what we have done before
* Create `x` sub-interfaces and equally spread `y` policy-maps between them.
    * try with 3000 sub-interfaces and 10 policy-maps

## Files that need to be edited

* Edit, add or remove any file needed, to create the expected output.

## Example of expected outputs

The output below is an example. Any solution is valid as long as you have `x` sub-interfaces and equally spread `y` policy-maps between them.

```buildoutcfg
interface Gi0/0/0.1
 no shut
 policy-map policy-map 1
interface Gi0/0/0.2
 no shut
 policy-map policy-map 10
interface Gi0/0/0.3
 no shut
 policy-map policy-map 9
interface Gi0/0/0.4
 no shut
 policy-map policy-map 8
interface Gi0/0/0.5
 no shut
 policy-map policy-map 7
interface Gi0/0/0.6
 no shut
 policy-map policy-map 6
interface Gi0/0/0.7
 no shut
 policy-map policy-map 5
interface Gi0/0/0.8
 no shut
 policy-map policy-map 4
interface Gi0/0/0.9
 no shut
 policy-map policy-map 3
interface Gi0/0/0.10
 no shut
 policy-map policy-map 2
interface Gi0/0/0.11
 no shut
 policy-map policy-map 1
interface Gi0/0/0.12
 no shut
 policy-map policy-map 10
```