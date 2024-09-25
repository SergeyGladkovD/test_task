from django.contrib import admin
from .models import NetworkNode, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'level', 'supplier', 'debt_to_supplier', 'created_at')
    list_filter = ('city',)
    inlines = [ProductInline]

    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0)
        self.message_user(request, "Задолженности очищены.")

    clear_debt.short_description = "Очистить задолженности выбранных узлов"


admin.site.register(NetworkNode, NetworkNodeAdmin)
admin.site.register(Product)
