#coding:utf8
from django.db import models
import os
from PIL import Image
from Airblog.settings import MEDIA_ROOT
from django.db.models.fields.files import ImageFieldFile


def make_thumb(path, size=600):
    imgBuf = Image.open(path)
    width, height = imgBuf.size
    if width > size:
        delta = width / size
        height = int(height / delta)
        imgBuf.thumbnail((size, height), Image.ANTIALIAS)
        return imgBuf
    

class Category(models.Model):
    '''文章分类模型'''
    # 分类名称
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        '''模型元数据'''
        # 数据库表名
        db_table = 'article_category'


class Tag(models.Model):
    '''文章标签模型'''
    # 标签名称
    tag_name = models.CharField(max_length=20, blank=True)
    # 标签创建时间
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.tag_name)

    class Meta:
        '''模型元数据'''
        # 数据库表名
        db_table = 'article_tag'


class Author(models.Model):
    '''作者模型'''
    # 作者名称
    name = models.CharField(max_length=30)
    # 作者邮箱
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        '''模型元数据'''
        # 数据库表名
        db_table = 'article_author'


class Article(models.Model):
    '''文章模型'''
    # 文章标题
    title = models.CharField(max_length=50)
    # 文章作者
    author = models.ForeignKey(Author)
    # 文章分类
    category = models.ForeignKey(Category)
    # 文章标签
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章发布时间
    publish_time = models.DateTimeField(auto_now_add=True)
    # 文章更新时间
    update_time = models.DateTimeField(auto_now=True)
    # 文章内容
    content = models.TextField()

    def __unicode__(self):
        return u'%s %s %s' % (self.title, self.author, self.publish_time)

    class Meta:
        '''模型元数据'''
        # 数据库表名
        db_table = 'article'
        # 按发布时间倒序排列
        ordering = ['-publish_time',]


class Media(models.Model):
    '''文章媒体超类'''
    # 上传时间
    upload_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)
    # 关联的文章
    article = models.ForeignKey(Article)

    class Meta:
        '''模型元数据'''
        # 定义 Media 为抽象类，只用于被子类继承
        abstract = True
        # 按上传时间倒序排列
        ordering = ['-upload_time',]


class Images(Media):
    '''文章配图'''
    # 上传图片URL
    image = models.ImageField(upload_to='upload_images', blank=True)
    # 缩略图URL
    thumb = models.ImageField(upload_to='upload_images/thumb_images', blank=True)

    def __unicode__(self):
        imgName = self.image.name
        return u'%s %s' % (imgName, self.article.title)

    def save(self, *args, **kwargs):
        base, ext = os.path.splitext(os.path.basename(self.image.path))
        super(Images, self).save()
        thumbBuf = make_thumb(os.path.join(MEDIA_ROOT, self.image.name))
        if thumbBuf:
            relate_thumb_path = os.path.join('upload_images/thumb_images/', base + '.thumb' + ext)
            thumb_path = os.path.join(MEDIA_ROOT, relate_thumb_path)
            thumbBuf.save(thumb_path)
            self.thumb = ImageFieldFile(self, self.thumb, relate_thumb_path)
            super(Images, self).save()

    class Meta(Media.Meta):
        '''模型元数据'''
        # 数据库表名
        db_table = 'article_image'


class Files(Media):
    '''文章附件'''
    # 文章附件URL
    file_url = models.FileField(upload_to='upload_files/%Y/%m/%d', blank=True)

    def __unicode__(self):
        fileName = os.path.basename(self.file_url)
        return u'%s %s' % (fileName, self.article.title)

    class Meta(Media.Meta):
        '''模型元数据'''
        # 数据库表名
        db_table = 'article_file'
