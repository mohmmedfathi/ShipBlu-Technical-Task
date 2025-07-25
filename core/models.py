from django.db import models
from django.utils import timezone
from core.managers import SoftDeleteManager
class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    objects = SoftDeleteManager()
    all_objects = models.Manager()  # To access everything, even deleted

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()


    class Meta:
        abstract = True
