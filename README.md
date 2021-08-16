# authy
DB SCHEMA FOR ROLE AND ACCESS
class Access(TimeStampedUUIDModel):
    name = models.CharField('Access Name', max_length=50)
    type = models.CharField('Access type', max_length=100)
    is_active = models.BooleanField('Is Active', default=True)

class Role(TimeStampedUUIDModel):
    name = models.CharField('Role Name', max_length=50)
    access = models.ManyToManyField(Access, related_name='role_access', blank=True)
    is_active = models.BooleanField('Is Active', default=True)
