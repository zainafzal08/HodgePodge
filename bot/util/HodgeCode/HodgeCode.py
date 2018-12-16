from util.HodgeCode.Grammar import Grammar
from util.HodgeCode.Parser import Parser
from util.HodgeCode.Emitter import Emitter
from util.HodgeCode.VM import VM

#from Grammar import Grammar
#from Parser import Parser
#from Emitter import Emitter
#from VM import VM

async def run_eq(s, server):
    g = Grammar()
    p = Parser(g, s)
    e = Emitter(g)
    vm = VM(p.scanner.symbol_table)
    e.emit(p.root)
    try:
        await vm.run(e.code_mem, server)
    except ZeroDivisionError as e:
        return "_Bzzt_ Attempted Division by zero!"
    except Exception as e:
        return "_Bzzt_ Something went wrong evaulating that statement! Are you sure it's correctly formed?"
    v = vm.stack.pop()
    if type(v) == float and v-int(v) == 0:
        return int(v)
    return round(v,8)
