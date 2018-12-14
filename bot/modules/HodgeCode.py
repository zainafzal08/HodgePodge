from util.Response import Response
from util.HodgeCode.HodgeCode import run_eq

class HodgeCode:
    def __init__(self):
        pass

    async def message(self, context):
        context.apply("do (.*)")
        if context.match:
            return Response(await run_eq(context.group(0), context.location))
