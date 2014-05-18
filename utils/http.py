from exceptions import ResponseError


def response_sanity_check(r):
    if not r.ok:
        raise ResponseError('HTTP Status: {}\n{}'.format(r.status_code, r.text))