# a new import
from django.contrib import admin
from blogging.models import Post, Category
from django.db import models


# and a new admin registration
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

# Define an inline class here
class CategoryInLine(admin.TabularInline):
    model = Category.posts.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (CategoryInLine,)
