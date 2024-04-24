from django.contrib import admin
from .models import * 
# Register your models here.
admin.site.site_header = "Mess'er Administration"


class MessOwnerAdmin(admin.ModelAdmin):
    list_display = ['mess', 'user', 'contact']
    search_fields = ['state', 'district', 'address', 'mess']


class MessMenuAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'mess', 'contact', 'email', 'type']
    search_fields = ['full_name', 'email', 'mess', 'contact']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date', 'morning', 'evening']
    search_fields = ['customer', 'date']


admin.site.register(MessOwner, MessOwnerAdmin)
admin.site.register(MessMenu, MessMenuAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Contact)

