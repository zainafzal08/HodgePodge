from Grammar import Grammar
from Parser import Parser
from Emitter import Emitter
from VM import VM

g = Grammar()
p = Parser(g, "(1+1)*2+1-2")
e = Emitter(g)
vm = VM()
e.emit(p.root)
vm.run(e.code_mem)
print(vm.stack.data)
