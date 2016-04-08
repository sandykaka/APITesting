"""
logging api
~~~~~~~~~~~~~~~
    this help to get the log across the project
"""
import logging
import logging.config

def singleton(cls):
    instances = {}
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance(


    )

@singleton
class Logger():
    def __init__(self):
        logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
                '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        self.logr = logging.getLogger('root')