from django.contrib import admin
from .models import Category, TodoList

class TodoListAdmin(admin.ModelAdmin):
    display = ("title",  "created", "due_date")

class CategoryAdmin(admin.ModelAdmin):
    display = ("name")

admin.site.register(Category, CategoryAdmin)
admin.site.register(TodoList, TodoListAdmin)