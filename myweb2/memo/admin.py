from django.contrib import admin
from memo.models import Memo

class MemoAdmin(admin.ModelAdmin):
    # 관리자 사이트에서 표시할 내용을 담는다.
    list_display = ('writer', 'memo')

# 관리자 사이트에 등록
admin.site.register(Memo, MemoAdmin)