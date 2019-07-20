from django.db import models

# Create your models here.


class HotSpot(models.Model):

    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)
    repost = models.IntegerField()
    comment = models.IntegerField()
    approve = models.IntegerField()
    address = models.URLField()
    image = models.URLField(default='https://wx2.sinaimg.cn/crop.28.0.457.343.240/005v4nJEly1g2rlnbru7sj30ea09jwl0.jpg')

    # 排序
    class Meta:
        ordering = ['-id']


class FreshNews(models.Model):

    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)

    address = models.URLField()
    image = models.URLField()

    class Meta:
        ordering = ['-id']


class FunnyStory(models.Model):
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)
    repost = models.IntegerField()
    comment = models.IntegerField()
    approve = models.IntegerField()
    address = models.URLField()
    image = models.URLField(default='https://wx1.sinaimg.cn/thumb150/9b6feba7ly1g2qtanp6igj21l62dse07.jpg')

    # 排序
    class Meta:
        ordering = ['-id']


class Society(models.Model):
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)
    repost = models.IntegerField()
    comment = models.IntegerField()
    approve = models.IntegerField()
    address = models.URLField()
    image = models.URLField(default='https://wx2.sinaimg.cn/thumb150/9b6feba7ly1g2kjezpysej22c03401kz.jpg')

    # 排序
    class Meta:
        ordering = ['-id']


class Fashion(models.Model):
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)
    repost = models.IntegerField()
    comment = models.IntegerField()
    approve = models.IntegerField()
    address = models.URLField()
    image = models.URLField(default='https://wx4.sinaimg.cn/thumb150/9b6feba7ly1g35vpfaml8j222o340b2b.jpg')

    # 排序
    class Meta:
        ordering = ['-id']


class TopEvent(models.Model):
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)
    repost = models.IntegerField()
    comment = models.IntegerField()
    approve = models.IntegerField()
    address = models.URLField()
    image = models.URLField(default='https://wx1.sinaimg.cn/thumb150/9b6feba7ly1g37xa50pf8j222o340npe.jpg')

    # 排序
    class Meta:
        ordering = ['-id']


class TopList(models.Model):
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)
    repost = models.IntegerField()
    comment = models.IntegerField()
    approve = models.IntegerField()
    address = models.URLField()
    image = models.URLField(default='https://wx1.sinaimg.cn/thumb150/9b6feba7ly1g37xa50pf8j222o340npe.jpg')

    # 排序
    class Meta:
        ordering = ['-id']




