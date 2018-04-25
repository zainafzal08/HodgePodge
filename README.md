# Hodge Podge

The Best Boy™

A beautiful discord bot built to be expandable, useful and ever so cute.

## User


## Developer

Hi! I assume you are here because you want to either understand how hodge podge works or because you want to maybe help out by building a module!

If you are here to build a module, thanks for dropping in! I hope i can make the process a bit easier by walking you through how the module interface works. Keep reading below. If you want a complete overview of how things works jump down to the explanation section

#### Making a Module

> Intro

So to make a module you must make a class much like the classes in `modules/`.

Make a class that inherits from `Module` and just has a empty `__init__` method that calls the super `__init__` method.

Then import the Trigger decorator from the ModuleDecorator file.

Now within your class you can create functions that are triggered by hodge podge as such

```python
@Trigger(moduleInstance, regex, access)
def roll(self, context):
    print("Doing the Roll")
```

> Trigger decorator

The trigger decorator must take in
1. The module instance (i.e `self`)
2. The regex on which you want this function to be triggered (regex groups will be given to your function via `context`)
3. A access list specifying the roles that people must have to use. If empty everyone is assumed to have access

for example

```python
@Trigger(self, 'hodge podge do me a solid and roll a d(\d+)', [])
def roll(self, context):
    dice = int(context["groups"][1])
    print("Doing the Roll On A d%d dice!"%dice)
```

> context



## TODO

#### Deploy 1

- [X] get discord interface up
- [X] math module would be cool
- [X] start changelog
- [X] pick someone random in the chat

#### Deploy 2

- [ ] Database set up
- [ ] scoring
- [ ] personality module
- [ ] help docs system
- [ ] jacks conversion modules
- [ ] shortcut commands (!hp)
- [ ] rss feed / twitter feed stuff / github
- [ ] web interface for permissions tweeks/resets
  - perhaps don't rely on interface for permissions, just give each user a id and we db roles  

#### Deploy 3

1. process processRequest set up
2. voice channel stuff
3. proper logging
4. command chaining with "then"
- [] set up system where a commands can be run after [x] seconds. (timing module)
- [] bomb message

#### Deploy 4

1. spell search

#### Deploy 5

1. google search
2. machine learning
3. dnd Beyond
4. reminders
5. hodge podge uses nicknames/personalises output

#### code

1. parser module clash handling
2. fix role id generation to not be predictable and hackable lol
3. add in dbrequest restrict for paramaters

#### Features
- voice Channel
- Google Module
- CostCo Bot For Gold / integrate leonbot
- update personality module to know peoples names and birthdays etc.
- reminders
- have hodge podge respond to "who do you work for"
- have hodge podge respond to "what is love"
- have typo detection / more robust trigger questions
- integrate with DnD Beyond!
- nickname for channels
- override command to just make hodge podge say something
- mini learning algorithm to learn memes by observation (if a gif is sent what triggered it?)
  - Natural Language Processing
- Website for hodge podge command interface (www.zainafzal.com/hpci)
- update documentation to include default values for objects
- Add system to handle database failure connection with a hard restart :D
- Help command for each module (unified help system?? print out from github?)
- Module to have admin commands in bot
- Massive Change log
- binary translator / encryptor
- clean up heroku to have 2 project, a off test bot (that is on when in dev) and a on hodge podge
- if the database crashes he just spams every channel
- log system
- error message should be DISTRESSED BEEPING
- have spell search work with commas
- math expression evaluator
- quick commands i.e !hp for hodge podge
- give option to validate hodge podge (prepend command)
- remember command
- markcov chains -> conversations
- conversion module (ft->meters)
- pick someone random in the chat
- enemy tracking in dnd games
- use "then" to chain commands
- bomb message, any message with a "!!kill5" will be deleted by hodge podge in 5 seconds
- Feature to hide messages that are tagged as spoilers till someone clicks on them. 