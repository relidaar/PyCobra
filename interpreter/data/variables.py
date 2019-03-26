class Variables:
    variable_dict = {

    }

    @staticmethod
    def add(id, value):
        Variables.variable_dict[id] = value

    @staticmethod
    def get(id):
        if id in Variables.variable_dict:
            return Variables.variable_dict.get(id)
        else:
            RuntimeError('Invalid variable')
