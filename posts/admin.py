from django.contrib import admin

# Register your models here.
# 현재를 기준으로 models module로부터 Post class import
from .models import Post

admin.site.register(Post)