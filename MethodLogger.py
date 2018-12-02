from inspect import isfunction, ismethod


def MethodLogger(fnc):
    if not isfunction(fnc) and not isfunction(fnc):
        print(f"{fnc} is not a function or method")
        return fnc

    if len(fnc.__qualname__.split('.')) != 1:
        print(f"{fnc} is not an unbound method")
        return fnc

    def wrapper(*args, **kwargs):
        print("log", fnc, args, kwargs) # TODO: log here
        return fnc(*args, **kwargs)

    return wrapper

