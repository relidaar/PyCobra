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
    """Representing the abstract type"""
    type = attr.ib()
    value = attr.ib()


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
class BinaryExpression:
    left = attr.ib()
    right = attr.ib()
    operator = attr.ib()

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        mapping = {
            '+': left + right,
            '-': left - right,
            '*': left * right,
            '/': left / right,
            '==': left == right,
            '!=': left != right,
            '>=': left >= right,
            '<=': left <= right,
            '>': left > right,
            '<': left < right,
        }
        return mapping[self.operator]


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
        type = self.expression.type
        value = self.expression.value
        mapping = {
            'Integer': int(value),
            'Float': float(value),
            'Boolean': value == 'True',
        }
        Variables.add(self.id, mapping[type])


@attr.s
class Variable:
    id = attr.ib()

    def eval(self):
        return Variables.get(self.id)
