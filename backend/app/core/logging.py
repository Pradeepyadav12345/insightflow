import logging
import sys

from app.core.config import settings


logger = logging.getLogger("insightflow")
logger.setLevel(getattr(logging, settings.log_level.upper(), logging.INFO))
logger.propagate = False

if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}') )
    logger.addHandler(handler)
