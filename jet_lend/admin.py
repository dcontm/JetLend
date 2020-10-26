from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','patponymic',)

@admin.register(models.Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('investor', 'state',)

@admin.register(models.Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ('investor', 'serial', 'number',)

@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('investor', 'doc_title',)