from django.db import models

# Create your models here.

from django.db import models
import uuid

# Create your models here.
from authy.base import ENTITY_TYPE_CHOICES


class UUIDModel(models.Model):
    """ An abstract base class model that makes primary key `id` as UUID
    instead of default auto incremented number.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedUUIDModel(UUIDModel):
    """An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields with UUID as primary_key field.
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Access(TimeStampedUUIDModel):
    name = models.CharField('Access Name', max_length=50)
    type = models.CharField('Access type', max_length=100)
    is_active = models.BooleanField('Is Active', default=True)

    class Meta:
        verbose_name = 'Access'
        verbose_name_plural = 'Accesses'


class Role(TimeStampedUUIDModel):
    name = models.CharField('Role Name', max_length=50)
    access = models.ManyToManyField(Access, related_name='role_access', blank=True)
    is_active = models.BooleanField('Is Active', default=True)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
