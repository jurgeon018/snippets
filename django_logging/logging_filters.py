import logging
from django.http import UnreadablePostError
# from django.utils.log import RequireDebugFalse


class SpecialFilter(logging.Filter):
    def filter(self, record, *args, **kwargs):
        print(record)
        if record.exc_info:
            exc_type, exc_value = record.exc_info[:2]
            if isinstance(exc_value, UnreadablePostError):
                return False
        return True
