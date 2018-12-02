from inspect import isfunction, ismethod


def BoundMethodLogger(fnc):
    if not isfunction(fnc) and not isfunction(ismethod(fnc)):
        print(f"{fnc} is not a function or method")
        return fnc

    if len(fnc.__qualname__.split('.')) == 1:
        print(f"{fnc} is not a bound method")
        return fnc

    def wrapper(cls, *args, **kwargs):
        print("log", cls, args, kwargs) # TODO: log here
        return fnc(cls, *args, **kwargs)

    return wrapper