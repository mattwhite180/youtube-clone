from django.contrib import admin

from .models import Video, Tag, Note

admin.site.site_url = "/myapp"


class VideoAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "description")


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "video")


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "video",
        "description",
    )


admin.site.register(Video, VideoAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Note, NoteAdmin)
