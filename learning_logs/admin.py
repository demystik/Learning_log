from django.contrib import admin
#  Import the model we want to register
from learning_logs.models import Topic, Entry
# Register your models here and manage through admin site.
admin.site.register(Topic)
admin.site.register(Entry)