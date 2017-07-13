from django.contrib import admin
from .models import Post
from .models import Test
from .models import UploadFileModel



# Register your models here.
admin.site.register(Post)
admin.site.register(Test)
admin.site.register(UploadFileModel)
