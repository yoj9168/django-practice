from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model class - RDB의 table과 matching
class Post(models.Model):
# field의 이름 - data type
    # author = models.CharField(max_length=100)
    # ForeignKey로 사용하는 field
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    # user가 삭제되면 해당 user가 쓴 게시물도 삭제
    body = models.TextField()   # 본문
    image = models.ImageField(upload_to='posts', null=True)
    created_at = models.DateTimeField() # 작성일
    # User나 Post 둘 중 하나에만 추가해주면 된다
    liked_users = models.ManyToManyField(User, related_name='liked_posts')
# print(instance) 출력 format customizing - overriding
    def __str__(self):
        # return f'{self.author}: {self.body}'
        if self.user:   # 있을 때
            return f'{self.user.get_username()}: {self.body}'
        # 없을 때
        return f'{self.body}'