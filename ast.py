import attr


@attr.s
class Program:
    """Entry point for parser"""
    expressions = attr.ib()

    def eval(self):
        for expression in self.expressions:
            value = expression.eval()
            print('{} - {}'.format(type(value), value))


@attr.s(auto_attribs=True)
class Integer:
    """Representing the integer number"""
    value: int

    def eval(self):
        return int(self.value)


@attr.s(auto_attribs=True)
class Float:
    """Representing the float number"""
    value: float

    def eval(self):
        return float(self.value)


@attr.s(auto_attribs=True)
class String:
    """Representing the string"""
    value: str

    def eval(self):
        return self.value


@attr.s(auto_attribs=True)
class Boolean:
    """Representing the boolean type"""
    value: bool

    def eval(self):
        return bool(self.value)
