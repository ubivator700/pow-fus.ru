from django.contrib import admin
from .models import Users, Companies, Analytic, Action

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    exclude=('id',)

@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    exclude=('company_id',)

@admin.register(Analytic)
class AnalyticAdmin(admin.ModelAdmin):
    pass


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    pass
