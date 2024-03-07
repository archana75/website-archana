from django.contrib import admin
from django.utils.html import format_html
from pytube import extract
from .models import (
    Post,
    Event,
    Project,
    Student,
    Generation,
    Achievement,
    AchievementPhoto,
    Cms,
    Sliderimage,
    Program,
    ProgramPhoto,
    )
 
# Register your models here.
 
class PostAdmin(admin.ModelAdmin):
     def image(self):
        return format_html(f"<img src='{self.image.url}' width=100>")
     
     def save_model(self, request, obj, form, change):
         if not obj.pk:
             obj.created_by = request.user
         super().save_model(request, obj, form, change)
     
     list_display = ("id", image, "caption", "is_published", "created_at", "created_by")
     exclude = ['created_by']
 
class EventAdmin(admin.ModelAdmin):

        
    def get_description(self, obj):
        return obj.description[:100]+"..."
    
    get_description.short_description = "description"


    list_display = (
        "id",
        "title",
        "image",
        "get_description",
        "date_start",
        "date_end",
        "is_published",
        "attachment_link",
        "created_at",
        "created_by",
    )
 
class ProjectAdmin(admin.ModelAdmin):

    def image(self):
        return format_html (f"<img src='{self.image.url}' width=100>")
    
    def get_description(self, obj):
        return obj.description[:100]+"..."
    
    def logo(self):
        return format_html (f"<img src='{self.logo.url}' width=100>")
    
    def yt_thumbnail(self):
        if self.video_link: 
            video_id=extract.video_id(self.video_link)
            return format_html (f"<img src='https://img.youtube.com/vi/{video_id}/0.jpg' width=100>")

    yt_thumbnail.short_description = "youtube video"
    get_description.short_description = "description"

    list_display = (
        'id',
        'title',
        'get_description',
        image,
        logo,
        yt_thumbnail,
        'attachment_link',
        'is_published',
        'school_product',
        'created_at',
        'created_by'
    )

    search_fields = ('title', 'id', 'description')
 
class GenerationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'school_year',
        'is_active'
    )
 
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'nisn',
        'nis',
        'firstname',
        'lastname',
        'is_active',
        'generation'
    )

    search_fields = ('firstname', 'lastname',)

class AchievementPhotoAdmin(admin.TabularInline):

    model = AchievementPhoto

    def project_by(self, obj):
        return "obj.created_by"
    
    list_display = (
        'id',
        'photo',
        'created_at',
        # 'created_by'
    )
 
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'description',
        # 'project',
        'event_name',
        'is_published',
        'created_at',
        'created_by',
    )
 
    inlines = [AchievementPhotoAdmin,]

class CmsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'content',
    )

class SliderimageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'created_at',
        'created_by',
    )

class ProgramPhotoAdmin(admin.TabularInline):

    model = ProgramPhoto

    def project_by(self, obj):
        return "obj.created_by"
    
    list_display = (
        'id',
        'photo',
        'created_at',
        # 'created_by'
    )

class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'created_at',
        'created_by',
        
    )
    inlines = [ProgramPhotoAdmin,]

    
admin.site.register(Post, PostAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Generation, GenerationAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Cms, CmsAdmin)
admin.site.register(Sliderimage, SliderimageAdmin)
admin.site.register(Program, ProgramAdmin)
# admin.site.register(AchievementPhoto, AchievementPhotoAdmin)