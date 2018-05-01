# Changelog

#### Game Module
- Improved random number generator for less repetition in rolls
  - less 1's in a row
- more verbose calling regex for dice rolls
  - `hodge podge roll a fucken d20`
- better error messages for incorrect rolls
  - i.e `hodge podge roll a d0`
- Rolls now support modifiers
  - `hodge podge roll a d8 + 7`


#### Utility Module

- Now exists
- added basic math
  - `hodge podge calc 5+5`
  - `hodge podge calculate (7*3)^9*1-9`
- added `@someone` to pick someone random in the server
  - `hodge podge pick someone`
-  



#### General code

- Set up decorator design pattern and formal module interface for quick commands
- Set up parser to hook directly into the module interface and handle registeration
- added generic context, trigger and information interface to move away from relience on discord as a chat medium
- database is now entirely generic with a request dict structure modules can use.
- roles are now enforced at parse time
