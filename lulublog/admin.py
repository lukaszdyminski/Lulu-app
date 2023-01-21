from django.contrib import admin
from .models import *
from .forms import *


# the admin site search fields and filters related to LuluPost model


@admin.register(LuluPost)
class LuluPostAdmin(admin.ModelAdmin):
    list_filter = ["author", "user", "publ_date"]
    search_fields = ["title", "content"]


# the admin site search fields and filters related to PetPost model


@admin.register(PetPost)
class PetPostAdmin(admin.ModelAdmin):
    list_filter = ["author", "user", "pet_name", "pet_species", "publ_date"]
    search_fields = ["title", "content"]


# the admin site search fields and filters related to LuluPostComment model


@admin.register(LuluPostComment)
class LuluPostCommentAdmin(admin.ModelAdmin):
    list_filter = ["user", "rate", "publ_date"]
    search_fields = ["user", "content"]


# the admin site search fields and filters related to PetPostComment model


@admin.register(PetPostComment)
class PetPostCommentAdmin(admin.ModelAdmin):
    list_filter = ["user", "rate", "publ_date"]
    search_fields = ["user", "content"]


