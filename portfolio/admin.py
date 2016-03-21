from django.contrib import admin
#import model
from models import Project, Upload, Category, Tag, Post

#automated slug creation
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

class UploadAdmin(admin.ModelAdmin):
    list_display = ('project',)
    list_display_links = ('project',)

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
    model = Post
    prepopulated_fields = {'slug': ('publish',)}

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Upload, UploadAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post,PostAdmin)
