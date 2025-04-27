import os
import uuid
from django.conf import settings
from django.db import models
from django.db.models import Subquery


def get_title_photo_random_filename(instance, filename):
    extension = os.path.splitext(filename)[1]
    return '{}/{}_{}'.format(settings.TITLE_PHOTO_PATH, uuid.uuid4(), extension)


class SQCount(Subquery):
    template = "(SELECT count(1) FROM (%(subquery)s) _count)"
    output_field = models.IntegerField()

