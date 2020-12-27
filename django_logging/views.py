import logging


logger = logging.getLogger(__name__)


def view(request):
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    # logger.error("error", exc_info=True)
    logger.critical("critical")
    # logger.exception("Something bad happened")
    return ''
