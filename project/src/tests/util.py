class weight(object):
    """
    Simple decorator to add a __weight__ property to a function
    """
    def __init__(self, val):
        self.val = val

    def __call__(self, func):
        func.__weight__ = self.val
        return func


class tags(object):
    """
    Simple decorator to add a __tags__ property to a function
    """
    def __init__(self, *args):
        self.tags = args

    def __call__(self, func):
        func.__tags__ = self.tags
        return func
