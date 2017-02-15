from django.db import models
from django.utils import timezone
#from pip._vendor.appdirs import unicode


class Post(models.Model):
    '''
        고경준은 천재님이십니다333333333333333333333333333333333333333333333333333^________________^
        post 모델 ormmaping
    '''
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Test(models.Model):
    '''기것은 테스트를 위한 모델입니다 주의하세요 반드스

    '''

    name = models.TextField(max_length=250)
    password = models.TextField(max_length=250)
    sex = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()
