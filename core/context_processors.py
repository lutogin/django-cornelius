from core.get_config import get_config


def config(req):
    return {'configs': get_config()}
