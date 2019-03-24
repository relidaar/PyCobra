import attr


@attr.s
class Program:
    """Entry point for parser"""
    expressions = attr.ib()

    def eval(self):
        for expression in self.expressions:
            value = expression.eval()
            print('{}: {}'.format(type(value), value))


@attr.s
class Type:
    """Representing the abstract type"""
    value = attr.ib()
    type = attr.ib()


class Integer(Type):
    """Representing the integer type"""

    def eval(self):
        return int(self.value)


class Float(Type):
    """Representing the float type"""

    def eval(self):
        return float(self.value)


class String(Type):
    """Representing the string type"""

    def eval(self):
        return self.value[1:-1]


class Boolean(Type):
    """Representing the boolean type"""

    def eval(self):
        return bool(self.value)


@attr.s
class BinaryOperation:
    left = attr.ib()
    right = attr.ib()


class Add(BinaryOperation):
    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        left = str(left) if self.right.type == 'String' else left
        right = str(right) if self.left.type == 'String' else right

        return left + right


class Subtract(BinaryOperation):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Multiply(BinaryOperation):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Divide(BinaryOperation):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Modulo(BinaryOperation):
    def eval(self):
        return self.left.eval() % self.right.eval()
