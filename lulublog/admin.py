from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.


@admin.register(LuluPost)
class LuluPostAdmin(admin.ModelAdmin):
    list_filter = ["author", "user", "publ_date"]
    search_fields = ["title", "content"]


@admin.register(PetPost)
class PetPostAdmin(admin.ModelAdmin):
    list_filter = ["author", "user", "pet_name", "pet_species", "publ_date"]
    search_fields = ["title", "content"]


@admin.register(LuluPostComment)
class LuluPostCommentAdmin(admin.ModelAdmin):
    list_filter = ["user", "rate", "publ_date"]
    search_fields = ["user", "content"]


@admin.register(PetPostComment)
class PetPostCommentAdmin(admin.ModelAdmin):
    list_filter = ["user", "rate", "publ_date"]
    search_fields = ["user", "content"]


