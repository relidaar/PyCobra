import attr


@attr.s
class Program:
    """Entry point for parser"""
    statements = attr.ib()

    def eval(self):
        for statement in self.statements:
            statement.eval()

    def eval_debug(self):
        for statement in self.statements:
            value = statement.eval()
            print('{}: {}'.format(type(value), value))

    def eval_test(self):
        for statement in self.statements:
            return statement.eval()


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
        return self.value == 'True'


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


@attr.s
class Print:
    value = attr.ib()
    newline = attr.ib()

    def eval(self):
        if self.newline:
            print(self.value)
        else:
            print(self.value, end='')

