from django.urls import reverse
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

class Node(MPTTModel):
	name = models.CharField(max_length=55, unique=True)
	parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('nodes:node_detail', kwargs={'pk': self.pk, })

	class MPTTMeta:
		order_insertion_by = ['name']



