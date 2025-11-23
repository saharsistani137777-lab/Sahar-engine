class Environment:
    def __init__(self, outer=None):
        self.store = {}
        self.outer = outer

    def get(self, name):
        if name in self.store:
            return self.store[name]
        elif self.outer:
            return self.outer.get(name)
        else:
            raise Exception(f"Undefined variable '{name}'")

    def set(self, name, value):
        self.store[name] = value
        return value

def truthy(value):
    return bool(value)

