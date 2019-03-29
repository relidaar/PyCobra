import attr

from interpreter_module.variables import Variables


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
        left = self.left.eval()
        right = self.right.eval()

        left = str(left) if type(right).__name__ == 'str' else left
        right = str(right) if type(left).__name__ == 'str' else right

        return left + right


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


@attr.s
class IfStatement:
    condition = attr.ib()
    body = attr.ib()
    else_body = attr.ib()

    def eval(self):
        if self.condition.eval():
            for statement in self.body:
                statement.eval()
        elif self.else_body:
            for statement in self.else_body:
                statement.eval()


@attr.s
class TernaryStatement:
    body = attr.ib()
    condition = attr.ib()
    else_body = attr.ib()

    def eval(self):
        value = 0
        if self.condition.eval():
            value = self.body.eval()
        elif self.else_body:
            value = self.else_body.eval()

        return value


@attr.s
class WhileStatement:
    condition = attr.ib()
    body = attr.ib()

    def eval(self):
        while self.condition.eval():
            for statement in self.body:
                statement.eval()


@attr.s
class ForStatement:
    initialization = attr.ib()
    condition = attr.ib()
    iteration = attr.ib()
    body = attr.ib()

    def eval(self):
        self.initialization.eval()
        while self.condition.eval():
            for statement in self.body:
                statement.eval()

            self.iteration.eval()
