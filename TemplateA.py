#!/usr/bin/env python3
#
# (c) 2020 Yoichi Tanibayashi
#
"""
Description
"""
__author__ = 'Yoichi Tanibayashi'
__date__   = '2020'

from MyLogger import get_logger


class ClassA:
    """ClassA

    Attributes
    ----------
    attr1: type(int|str|list of str ..)
        description
    """
    _log = get_logger(__name__, False)

    def __init__(self, opt, debug=False):
        """constructor

        Parameters
        ----------
        opt: type
            description
        debug: bool
            debug flag
        """
        self._dbg = debug
        __class__._log = get_logger(__class__.__name__, self._dbg)
        self._log.debug('opt=%s')

        self._opt = opt

    def end(self):
        """end

        Call at the end of program
        """
        self._log.debug('doing ..')
        print('end of ClassA')
        self._log.debug('done')

    def method1(self, arg):
        """method1

        Parameters
        ----------
        arg: str
            description
        """
        self._log.debug('arg=%s', arg)

        print('%s:%s' % (arg, self._opt))

        self._log.debug('done')


"""以下、サンプル"""


class SampleApp:
    """Sample application class

    Attributes
    ----------
    obj: ClassA
        description
    """
    _log = get_logger(__name__, False)

    def __init__(self, arg, opt, debug=False):
        """constructor

        Parameters
        ----------
        arg: str
            description
        opt: str
            description
        """
        self._dbg = debug
        __class__._log = get_logger(__class__.__name__, self._dbg)
        self._log.debug('arg=%s, opt=%s')

        self._arg = arg
        self._opt = opt

        self.obj = ClassA(opt, debug=self._dbg)

    def main(self):
        """main
        """
        self._log.debug('')

        for a in self._arg:
            self.obj.method1(a)

        self._log.debug('done')

    def end(self):
        """end

        Call at the end of program.
        """
        self._log.debug('doing ..')
        self.obj.end()
        self._log.debug('done')


import click
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS, help='''
Description
''')
@click.argument('arg', type=str, nargs=-1)
@click.option('--opt', '-o', 'opt', type=str, default='def_value',
              help='sample option')
@click.option('--debug', '-d', 'debug', is_flag=True, default=False,
              help='debug flag')
def main(arg, opt, debug):
    """サンプル起動用メイン関数
    """
    _log = get_logger(__name__, debug)
    _log.debug('arg=%s, opt=%s', arg, opt)

    app = SampleApp(arg, opt, debug=debug)
    try:
        app.main()
    finally:
        _log.debug('finally')
        app.end()


if __name__ == '__main__':
    main()
