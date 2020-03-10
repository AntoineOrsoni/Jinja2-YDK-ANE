This section has two folders :
* `exercices` with the exercices and instructions,
* `solutions` with example of solutions.

## Exercices

### ncclient running config

* getting the running config from the device using `ncclient`
    * Open a NETCONF session using `ncclient`,
    * Get the running-configuration (XML) from the device

## Available methods of ncclient manager

Operations are defined [here](https://github.com/ncclient/ncclient/tree/master/ncclient/operations).

```
OPERATIONS = {
    "get": operations.Get,
    "get_config": operations.GetConfig,
    "get_schema": operations.GetSchema,
    "dispatch": operations.Dispatch,
    "edit_config": operations.EditConfig,
    "copy_config": operations.CopyConfig,
    "validate": operations.Validate,
    "commit": operations.Commit,
    "discard_changes": operations.DiscardChanges,
    "cancel_commit": operations.CancelCommit,
    "delete_config": operations.DeleteConfig,
    "lock": operations.Lock,
    "unlock": operations.Unlock,
    "create_subscription": operations.CreateSubscription,
    "close_session": operations.CloseSession,
    "kill_session": operations.KillSession,
    "poweroff_machine": operations.PoweroffMachine,
    "reboot_machine": operations.RebootMachine,
}
```