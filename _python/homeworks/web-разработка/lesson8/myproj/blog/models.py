import datetime

from django.db import models


class Post(models.Model):
	date = models.DateTimeField('дата', default=datetime.datetime.now)
	title = models.CharField('заголовок', max_length=250)
	text = models.TextField('текст', help_text='текст записи блога')

	class Meta:
		verbose_name = 'запись блога'
		verbose_name_plural = 'записи блога'

	def __str__(self):
		return self.title
			
			
