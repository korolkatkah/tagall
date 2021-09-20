# спс за дай модуль
import logging
import requests
from .. import loader, utils

logger = logging.getLogger(__name__)

def register(cb):
    cb(TagAllMod())

