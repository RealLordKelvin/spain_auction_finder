from django.contrib import admin

# Register your models here.

from .models import AuctionInfo

admin.site.register(AuctionInfo)