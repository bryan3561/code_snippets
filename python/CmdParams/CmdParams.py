from sys import argv


class CmdParams:

    def __init__(self):
        pass

    @staticmethod
    def get_all():
        params = {}

        for param in argv[1:]:

            if "=" not in param:
                continue

            param_parts = param.split("=")

            param_key = param_parts[0]
            param_value = param_parts[1]

            params[param_key] = param_value

        return params

    def get(self, key):
        params = self.get_all()

        if key in params:
            return params[key]
        else:
            return False


def main():
    cmd = CmdParams()

    print(cmd.get('name'))
    print(cmd.get('lastName'))


if '__main__' == __name__:
    main()
