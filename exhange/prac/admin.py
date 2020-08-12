from django.contrib import admin
from .models import stocks,trade
# Register your models here.
class StockAdmin(admin.ModelAdmin):
    list_display = ('user', 'stock1', 'stock2')
class TradeAdmin(admin.ModelAdmin):
    list_display=('seller','quantity','stock','buyer')
admin.site.register(stocks,StockAdmin)
admin.site.register(trade,TradeAdmin)
