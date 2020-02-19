# Django3_Ueditor
Django3中使用Ueditor富文本编辑器

![avatar](https://github.com/zzy0371/Django3_Ueditor/blob/master/%E5%85%AC%E4%BC%97%E5%8F%B7.jpg)

Ueditor目前不支持Django3 。
如果在Django3中使用Ueditor需要使用本项目提供的Ueditor应用包。

## 一、	下载django3.0.3(本教程测试版本)  
## 二、	创建项目
django-admin startproject django_ueditor
## 三、	创建应用
python manage.py startapp article
## 四、	拷贝Django_Ueditor到自己的项目
将article拷贝新建的apps中，将Django_Ueditor拷贝到extract_apps中
将apps与extract_apps标记为项目根目录
在settings.py中添加路径配置
Import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
sys.path.insert(0,os.path.join(BASE_DIR,'extract_apps'))
## 五、	新建模型类 
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="文章标题")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
body = UEditorField(imagePath='imgs/',width='100%')
## 六、	注册应用  
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
    'DjangoUeditor'
]
#  七、	生成迁移文件
此时会出现如下错误 
No module named 'django.utils.six'
可以将django2中的django.utils.six.py 文件拷贝到django.utils目录中
python manage.py makemigrations  
即可生成迁移文件成功

#  八、	执行迁移文件
python manage.py migrate
#  九、	创建超级管理员
python manage.py createsuperuser

#  十、	启动服务器
python manage.py runserver

#  十一、	进入后台管理
http://127.0.0.1:8000/admin/
#  十二、	添加文章
http://127.0.0.1:8000/admin/article/article/add/
会出现错误
render() got an unexpected keyword argument 'renderer'
此时需要在django\forms\boundfield.py 中注释掉96行
# renderer=self.form.renderer,
到此为止即可出现文章正文的富文本页面

#  十三、	添加图片
注意此时单张图片添加按钮为禁用，多张为启用
但是此时点击添加多张图片则出现错误
后端配置项没有正常加载，上传插件不能正常使用！
需要配置DjangoUeditor的路由文件
在项目路由下配置
path('ueditor/', include('DjangoUeditor.urls')),
此时单张图片添加按钮也为启用状态

#  十四、	添加媒体资源配置
此时如果需要正确的管理添加的媒体资源需要 在settings.py中配置如下信息

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIAFILES_DIRS = [os.path.join(BASE_DIR,'media')]
配置过之后上传的资源都会出现在media目录

错误1：上传多张图片会出现不能预览
需要在项目路由下配置媒体资源路由
from django.conf.urls import url
from django.views.static import serve
from .settings import MEDIA_ROOT
url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
此时上传多张图片可以预览


错误2、点击上传单张图片则会出现错误 
Refused to display  in a frame because it set 'X-Frame-Options' to 'deny'.
解决方法
在settings.py中添加配置
X_FRAME_OPTIONS = 'sameorigin'


