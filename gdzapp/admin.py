from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Cover)
admin.site.register(Subject)
admin.site.register(Task)
admin.site.register(TaskImage)
admin.site.register(Parts)