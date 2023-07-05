from django.contrib import admin
from .models import *

admin.site.register(Column)
admin.site.register(Task)
admin.site.register(Tab)
admin.site.register(Param)
admin.site.register(Record)
admin.site.register(RecordParam)