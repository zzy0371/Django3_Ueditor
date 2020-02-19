from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="文章标题")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    body = UEditorField(imagePath='imgs/',width='100%')