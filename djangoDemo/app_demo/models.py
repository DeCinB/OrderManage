from django.db import models
#数据模块，设计数据库
# Create your models here.
class Article(models.Model):

	article_id=models.AutoField(primary_key=True)
	title=models.TextField()
	brief_content=models.TextField()
	content=models.TextField()
	publish_date=models.DateTimeField(auto_now=True) 

	def __str__(self):
		return self.title