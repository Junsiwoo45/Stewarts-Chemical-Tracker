from django.contrib import admin
from .models import LawnItem
from .models import PestItem
from .models import TreeItem




# Register your models here.
admin.site.register(LawnItem)
admin.site.register(PestItem)
admin.site.register(TreeItem)
