from optparse import make_option

from django.core.management.base import NoArgsCommand

from websettings import websettings


class Command(NoArgsCommand):
    """print_websettings command"""

    help = "Print the active websettings."
    option_list = NoArgsCommand.option_list + (
        make_option('--format', default='simple', dest='format',
                    help='Specifies output format.'),
        make_option('--indent', default=4, dest='indent', type='int',
                    help='Specifies indent level for JSON'),
    )

    def handle_noargs(self, **options):
        output_format = options.get('format', 'json')
        settings_dict = dict((k, v) for k, v in websettings)
        indent = options.get('indent', 4)

        if output_format == 'json':
            self.print_json(settings_dict, indent)
        else:
            self.print_simple(settings_dict)

    @staticmethod
    def print_json(settings_dict, indent):
        try:
            import json
        except ImportError:
            import simplejson as json
        print(json.dumps(settings_dict, indent=indent))

    @staticmethod
    def print_simple(settings_dict):
        for key, value in settings_dict.items():
            print('%-40s = %r' % (key, value))
