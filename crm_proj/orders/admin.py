from django.contrib import admin

from .models import Devices, Order, Customer, DeviceInField


class DevicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'model')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_address', 'customer_city')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'customer', 'order_description', 'created_dt',
                    'last_update_dt', 'order_status')


class DeviceInFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial_number', 'customer_id', 'analyzer_id', 'owner_status')


admin.site.register(Devices, DevicesAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(DeviceInField, DeviceInFieldAdmin)
