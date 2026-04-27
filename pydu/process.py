try:
    import psutil
except ImportError:
    raise ImportError('Need to pip install psutil if you use pydu.process')

from .path import is_super_path


def get_processes_by_path(path):
    """
    Get processes which are running on given path or sub path of given path.
    """
    pass
