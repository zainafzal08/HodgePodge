import logging
hodge_logger = logging.getLogger('hodge_podge')
hodge_logger.setLevel(logging.DEBUG)
user_module_logger = logging.getLogger('user_module')
user_module_logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

hodge_logger.addHandler(ch)
user_module_logger.addHandler(ch)
