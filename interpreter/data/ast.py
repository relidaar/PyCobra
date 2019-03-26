import attr

from interpreter.data.variables import Variables


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
    value = attr.ib()


class Integer(Type):
    def eval(self):
        return int(self.value)


class Float(Type):
    def eval(self):
        return int(self.value)


class String(Type):
    def eval(self):
        return self.value[1:-1]


class Boolean(Type):
    def eval(self):
        return self.value == 'True'


@attr.s
class BinaryExpression:
    left = attr.ib()
    right = attr.ib()


class Addition(BinaryExpression):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Subtraction(BinaryExpression):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Multiplication(BinaryExpression):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Division(BinaryExpression):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Modulo(BinaryExpression):
    def eval(self):
        return self.left.eval() % self.right.eval()


class Equals(BinaryExpression):
    def eval(self):
        return self.left.eval() == self.right.eval()


class NotEqual(BinaryExpression):
    def eval(self):
        return self.left.eval() != self.right.eval()


class LessThan(BinaryExpression):
    def eval(self):
        return self.left.eval() < self.right.eval()


class LessThanOrEquals(BinaryExpression):
    def eval(self):
        return self.left.eval() <= self.right.eval()


class GreaterThan(BinaryExpression):
    def eval(self):
        return self.left.eval() > self.right.eval()


class GreaterThanOrEquals(BinaryExpression):
    def eval(self):
        return self.left.eval() >= self.right.eval()


class And(BinaryExpression):
    def eval(self):
        return self.left.eval() and self.right.eval()


class Or(BinaryExpression):
    def eval(self):
        return self.left.eval() or self.right.eval()


@attr.s
class Print:
    value = attr.ib()
    newline = attr.ib()

    def eval(self):
        value = self.value.eval()
        if self.newline:
            print(value)
        else:
            print(value, end='')


@attr.s
class Assignment:
    id = attr.ib()
    expression = attr.ib()

    def eval(self):
        Variables.add(self.id, self.expression.eval())


@attr.s
class Variable:
    id = attr.ib()

    def eval(self):
        return Variables.get(self.id)
