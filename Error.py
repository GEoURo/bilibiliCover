class Error(Exception):
    '''Base Error class for exception message'''
    pass

class addrError(Error):
    def __init__(self, msg):
        self.msg = msg


class aidError(Error):
    def __init__(self, msg):
        self.msg = msg

