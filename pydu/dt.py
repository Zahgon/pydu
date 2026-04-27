import time


class timer(object):
    """
    A timer can time how long does calling take as a context manager or decorator.
    If assign ``print_func`` with ``sys.stdout.write``, ``logger.info`` and so on,
    timer will print the spent time.
    """

    def __init__(self, print_func=None):
        self.elapsed = None
        self.print_func = print_func

    def __enter__(self):
        pass

    def __exit__(self, *_):
        pass

    def __call__(self, fun):
        pass

    def __str__(self):
        pass
