from django.conf import settings
from django.db import models
from django.utils import timezone

# Define our model, another word, this is the object
"""
classはオブジェクトを定義してますよ、ということを示すキーワードです。
Post はモデルの名前で、他の名前をつけることもできます（が、特殊文字と空白は避けなければいけません）。
モデルの名前は大文字で始めます。
models.Model はポストがDjango Modelだという意味で、
Djangoが、これはデータベースに保存すべきものだと分かるようにしています。
"""
class Post(models.Model):
    '''
    models.CharField – 文字数が制限されたテキストを定義するフィールド
    models.TextField – これは制限無しの長いテキスト用
    models.DateTimeField – 日付と時間のフィールド
    models.ForeignKey – これは他のモデルへのリンク
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    # Define the method for the object
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
