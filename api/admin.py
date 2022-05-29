from django.contrib import admin
from .models import Employee, PointOfSale, Visit


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone')
    search_fields = ('first_name',)


class PointOfSaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'employee')
    search_fields = ('title',)


class VisitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'visitor', 'point_sale')
    search_fields = ('visitor__first_name', 'point_sale__title')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(PointOfSale, PointOfSaleAdmin)
admin.site.register(Visit, VisitAdmin)
