class ResponseError(Exception):
    """An error response was received from a HTTP request."""
    pass

class ThresholdReached(Exception):
    """A threshold has been reached."""
    pass