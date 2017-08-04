from django.contrib import admin

# Register your models here.
import models
admin.site.register(models.Employee)
admin.site.register(models.Department)
admin.site.register(models.Position)
admin.site.register(models.UserProfile)
admin.site.register(models.Group)