from ratpack.server import RatpackServer
from ratpack.func import Action
from app.Helpers import *
from chain import *

def sfn(spec):
    spec.handlers(act(handlers))

RatpackServer.start(act(sfn))