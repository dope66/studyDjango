from django.db import models
from user.models import User

class Board(models.Model):

    b_title = models.CharField(max_length=10)
    b_author = models.ForeignKey(User,on_delete=models.CASCADE)
    b_content = models.CharField(max_length=2000)
    b_date =models.DateTimeField(auto_now=True)
    b_like=models.IntegerField(default=0)
    b_comment_count= models.IntegerField(default=0)

    def __str__(self):
        return self.b_title


class Comment(models.Model):

    c_author= models.ForeignKey(User,on_delete=models.CASCADE)
    c_content = models.CharField(max_length=50)
    c_board = models.ForeignKey(Board,on_delete=models.CASCADE)

    def __str__(self):
        return self.c_content