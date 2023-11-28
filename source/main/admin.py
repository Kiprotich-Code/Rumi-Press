from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Authors, Books, Category, Publisher, Expense

# Register your models here.
admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Expense)