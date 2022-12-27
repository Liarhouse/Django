from django.contrib import admin
from member.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_pw', 'tel', 'email')


admin.site.register(Member, MemberAdmin)
