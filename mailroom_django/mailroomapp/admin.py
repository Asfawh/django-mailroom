# Register models here.
from django.contrib import admin
from mailroomapp.models import User, Donor, Donations

admin.site.register(User)
admin.site.register(Donor)
admin.site.register(Donations)
