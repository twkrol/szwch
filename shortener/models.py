import random
import string

from django.db import models

TRACKING_CODE_LENGTH = 8


def _make_short_code():
    new_code = ''.join(random.choice(string.ascii_lowercase) for i in range(TRACKING_CODE_LENGTH))
    return new_code


class Link(models.Model):
    target = models.CharField(max_length=1024)
    short = models.CharField(max_length=TRACKING_CODE_LENGTH, default=_make_short_code)
