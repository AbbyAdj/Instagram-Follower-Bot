import time

class NoDetailsProvided(BaseException):
    pass

def wait(seconds_to_wait):
    """Pause for a certain number of seconds"""
    time.sleep(seconds_to_wait)

