import os
import sys

debug = os.environ["DEBUG"] == "yes"


def print_debug(*args, **kwargs):
    if(debug):
        print(*args, **kwargs)


def print_error(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr, flush=True)


def fail(e):
    if(debug and isinstance(e, BaseException)):
        raise e
    print_error(e)
    exit(1)


def handle_exception(*exceptions):
    def wrapper(function):
        def customized_function(*args, **kwargs):
            try:
                function(*args, **kwargs)
            except (exceptions) as e:
                fail(e)
        customized_function.__wrapped__ = True
        return customized_function
    return wrapper
