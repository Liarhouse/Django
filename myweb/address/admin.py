from django.contrib import admin
from address.models import Address

# Admin 사이트(관리자 페이지)에 반영될 내용을 기술한다.
class AddressAdmin(admin.ModelAdmin):
    # 관리자 페이지에 표시할 항목(필드)을 튜플로 지정
    list_display = ('name', 'tel', 'email', 'address')

# 클래스 등록
admin.site.register(Address, AddressAdmin)