from django.db import models

class ActiveObjects(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)