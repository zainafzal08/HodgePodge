# Hodge Podge

The Best Boy™

A beautiful bot built to help out by interacting with various chat and web interfaces.

Built from the ground up to be modular, expandable and low key adorable.

## Modules

Hi! I assume you are here because you want to either understand how hodge podge works or because you want to maybe help out by building a module!

If you are here to build a module, thanks for dropping in! I hope i can make the process a bit easier by walking you through how the module interface works. Keep reading below.

#### Making a Module

> Intro

For this documentation we are gonna go through making a simple module called Utility.

So to make a module you must make a class much like the classes in `modules/`.

Make a class that inherits from `Module` and just has a empty `__init__` method that calls the super `__init__` method.

```python
from modules.Module import Module, Trigger

class Utility(Module):
    def __init__(self):
        super().__init__("Utility")
```

Now within your class you can create functions that are triggered by hodge podge by using the `Trigger` decorator as such

```python
@Trigger(moduleInstance, regex, access)
def myFunc(self, context):
    # some logic
```

> Trigger decorator

The trigger decorator must take in
1. The regex on which you want this function to be triggered (regex groups will be given to your function via `context`)
2. A list which assigns a identifier string to each group.

for example

```python
@Trigger('hi my name is (\w+)', ["name"])
def sayHi(self, context):
  name = context.groups[0]
```

The function you bind to this decorator _must_ have the prototype

`def f(self, context)`

you may change the name of the context object but it must take in the context and a reference to the module object.

> context

The context object is how your module gets information on why it's been woken up and the current state of the chat. It contains the following fields.

| Field  | Type      | Description                   |
| ------ | --------- | ---------------------------- |
| groups | list(str/None) | List of matched regex groups in order of appearance in the regex (non matched groups still appear in this list but have a None value) |
| locationId | str | A unique id the triggering interface has given to the chat that triggered you |
| raw | str | the raw string that caused the trigger |
| getNumber | int function(int) | takes in index of 1 matched group and returns it as a integer |
| getString | str function(int) | takes in index of 1 matched group and returns it as a string |
| getUser | User function() | returns the user object of the person who caused the triggered |
| getMembers | list(User) function() | returns a list of users in the chat in which the trigger originated |
| getGroup | str/None function(str) | returns a matched group by it's given id in the trigger decorator |

Most of the functions are provided for convenience, for example consider

```python
@Trigger('hi my name is (\w+)', ["name"])
def sayHi(self, context):
  # all do the same thing.
  name = context.groups[0]
  name = context.getString(0)
  name = context.getGroup("name")
```

> Validation

Now something that comes up a lot with a chat bot is people triggering it incorrectly and you wanting to give a meaningful error message or a "fuck you" message depending on if your friends are like mine and try to break your boy.

Your module has a function predefined called "validate" which is called before your actual trigger handler function is called.

It has the following prototype

```python
def validate(self, raw, id):
    return None
```

it is called on every group on the trigger (which is passed in as raw) which it identifies via the id you gave it (None if you didn't give it one)

You can override this with your own logic, simply return None if the input is valid to trigger your normal handler or return a string with a error message inside for the bot to respond with.

Consider the following
