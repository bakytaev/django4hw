from django.contrib import admin
from .models import Block, Owner


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    pass


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'purchase_date',)
    date_hierarchy = 'purchase_date'


# admin.site.register(Block)
# admin.site.register(Owner)

# Register your models here.
