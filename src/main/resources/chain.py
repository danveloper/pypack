from ratpack.handling import Handler

class StandaloneHandler(Handler):
    def handle(self, ctx):
        ctx.render("Hello from standalone handler!")

def handlers(chain):
    chain.get(lambda ctx :
        ctx.render("Hello World!")
    ).get("foo", lambda ctx :
        ctx.render("Hello Foo!")
    ).get("other", StandaloneHandler())