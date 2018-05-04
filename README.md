# Hodge Podge

The Best Boy™

A beautiful bot built to help out by interacting with various chat and web interfaces.

Built from the ground up to be modular, expandable and low key adorable.

## Linking

Hey! Are you here because you use hodge pogde on multiple apps and wish to have your accounts linked? Nice!

Simply go onto one of the apps you already have user data for and type in `hodge podge what's my id` and hodge podge will give you a one time use identifier

> this doesn't expire so make sure you use it before someone else does!

Then go to the app you just put hodge podge into and say `hodge podge my id is <id>`
and hodge podge will remove all your user data in that app and relink you so both apps reference the same user data.

You can do this as many times as you like but do note hodge podge doesn't merge your user data, it just propegates one user object. (if your wondering why he doesn't merge them it's because i'm lazy and that makes the whole process a lot more complicated.)

Now because this isn't automatic you can have multiple accounts with hodge podge depending on use. i.e you can have a different wholesome account on discord and messenger but then a naughty account on IRC and Slack. (assuming in the future these interfaces even exist.)

## Modules

Hi! I assume you are here because you want to either understand how hodge podge works or because you want to maybe help out by building a module!

If you are here to build a module, thanks for dropping in! I hope i can make the process a bit easier by walking you through how the module interface works. Keep reading below.

#### Intro

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

#### Trigger decorator

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

#### context

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

> Note that the getGroup is provided for convience but can not be relied upon, the purpose of group id's is for validation (below) so if you give 2 groups the same id in a trigger the getGroup() function returns the last instance.

#### Validation

Now something that comes up a lot with a chat bot is people triggering it incorrectly and you wanting to give a meaningful error message or a "fuck you" message depending on if your friends are like mine and try to break your boy.

Your module has a function predefined called "validate" which is called before your actual trigger handler function is called.

It has the following prototype

```python
def validate(self, raw, id):
    return None
```

it is called on every group on the trigger (which is passed in as raw) which it identifies via the id you gave it ("None" if you didn't give it one)

You can override this with your own logic, simply return None if the input is valid to trigger your normal handler or return a string with a error message inside for the bot to respond with on error.

Consider the following

```python
@Trigger('roll a d(\d+)',["d"])
def roll(self, context):
    diceType = context.getNumber(0)
    roll = rollDice(diceType)
```

This should trigger on `roll a d20` or `roll a d10` but obviously we can't roll a d0 and we want to set a upper limit rather then trying to handle behaviour of trying to roll a d100000000. So we override the validate function.

```python
def validate(self, raw, id):
  if id == "d":
    if int(raw) <= 0 or int(raw) > 10000:
      return "I can only handle d1 to d10000!"
  return None
```

> Notice how the "id" parameter allows us to have different rules for differing groups.

Now if we trigger it correctly such as `roll a d10` the validate function returns `None` signalling valid input and the dice is rolled.
Otherwise the error message is thrown back and the bot will respond with it automatically.

> If multiple groups are invalid only the first invalid one throws a error, there are not cascading errors.

Something worth noting is that this function is class wide. So if you reuse a id across multiple triggers the same rules are applied. Which is intentional, although it might seem intuitive to have a different id namespace per function, many parameters are repeated within a module. Consider "roll a dice" and "roll 2 dice". one will take in 1 diceType and the other 2 but all 3 of the dice type inputs are subject to the same validity rules so giving them all the same id makes validation a lot easier.

#### Response

Cool we can do fancy logic and get triggered, Now how do we actually send something back to the user?

All interaction from the module to the bot goes through the `Response` and `Request` objects.

The `Response` object is how your module can respond to a trigger. if you do not return a response object the user has no way of telling it was triggered.

**TODO: put in docs for response object**

Consider out dice rolling example again

```python
@Trigger('roll a d(\d+)',["d"])
def roll(self, context):
    diceType = context.getNumber(0)
    resText = "It landed on %s"%rollDice(diceType)
    # make a Response objects
    res = Response()
    # declare a text response
    res.textResponce(resText, context.locationId, "output")
    # return
    return res
```

#### Request
**TODO: put in docs for request object**

## Interfaces

Hodge podge can interact with multiple different forms of input in the form of interfaces. A interface is a object that runs on it's own thread that interacts with the outside world (either through a website or api or whatever) and passes messages and state info about a certain chat to hodge podge so he can respond.

As long as the interface can run on a thread and can call the "talk" method with hodge podge, it will work. Wanna connect hodge podge up to a irc? go for it! set up some code to listen in and pass the messages to hodge podge and format/send back the result.

#### Intro

A interface must have a init function which takes in a threadID (for tracking purposes) and a reference to hodge podge so you can trigger commands.

In `run.py` each interface is given a threadId and a reference to hodge podge and started on it's own thread. Because of the fact that we have concurrent processes hodge podge calls modules asyncronously. Once the module responds, the response will be ushered onto the interface.

This allows hodge podge to function even with a slow or unreliable modules. The  interfaces though has to conform to this async approach.

Hodge podge will return from a talk request immediately, the function is a wrapper which basically triggers the relevant modules and then adds your message to a queue waiting for the modules to respond.
Once the modules respond the supplied callback function is triggered with the response.

#### Users
