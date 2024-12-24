import vidtoolz


def create_parser(subparser):
    parser = subparser.add_parser("{{cookiecutter.entry_name}}", description="{{ cookiecutter.description or "" }}")
    # Add subprser arguments here.
    parser.add_argument("-test", "--test", type=str, help="Example argument")
    return parser


class ViztoolzPlugin:
    """ {{ cookiecutter.description or "" }} """
    __name__ = "{{cookiecutter.entry_name}}"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.hello)
    
    def hello(self, args):
        # this routine will be called when "vidtoolz "{{cookiecutter.entry_name}} is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")

{{cookiecutter.entry_name}}_plugin = ViztoolzPlugin()
