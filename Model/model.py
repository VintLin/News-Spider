from vSQL.vorm import Module
from vSQL.vattr import *


class News(Module):
    id = column(zintger(20), isAutocount=True, isPrimary=True, isNotnull=True)
    filename = column(zchar(80), isNotnull=True)
    path = column(zchar(100), isNotnull=True)
    website = column(zchar(20), isNotnull=True)
    title = column(zchar(80), isNotnull=True)
    time = column(zdatetime(), isNotnull=True)
    type = column(zchar(20), isNotnull=True)

