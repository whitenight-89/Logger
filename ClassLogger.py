from inspect import isclass, ismethod, isfunction


def ClassLogger(cls=None, includes=[], excludes=[], include_private_methods=True):
    if cls:
        return _ClassLogger(cls, includes, excludes, include_private_methods)
    else:
        def wrapper(cls):
            return _ClassLogger(cls, includes, excludes, include_private_methods)
        return wrapper


class _ClassLogger:
    def __init__(self, cls, includes, excludes, include_private_methods):
        self.cls = cls
        self.includes = [includes] if isinstance(includes, str) else includes
        self.excludes = [excludes] if isinstance(excludes, str) else excludes
        self.include_private_methods = include_private_methods

    class Deco:
        def __init__(self, instance, fnc):
            self.instance = instance
            self.fnc = fnc

        def __call__(self, *args, **kwargs):
            print("log", self.fnc, args, kwargs) # TODO: log here
            return self.fnc(self.instance, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        if not isclass(self.cls):
            print(f"{self.cls} is not a class")
            return self.cls.__call__(*args, **kwargs)

        cls_instance = self.cls(*args, **kwargs)

        for name, method in self.cls.__dict__.items():
            if not self._needs_to_be_decorated(name, method):
                continue

            cls_instance.__setattr__(name, self.Deco(cls_instance, method))

        return cls_instance

    def _needs_to_be_decorated(self, name, method):
        if not ismethod(method) and not isfunction(method):
            return False

        if name in self.excludes:
            return False

        if name in self.includes:
            return True

        if name.startswith("__"):
            return False

        if not self.include_private_methods and name.startswith("_"):
            return False

        return True
