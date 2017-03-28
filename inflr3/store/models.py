from django.db import models
from django.conf import settings
# Create your models here.

class ProductManager(models.Manager):

    def search(self,query):
        return self.get_queryset().filter(
            models.Q(name__incontains = query) | \
            models.Q(description__incotains = query)
        )

class Product(models.Model):

    name = models.CharField('Nome do Produto',max_length=100)
    slug = models.SlugField('Atalho')
    image = models.ImageField(upload_to='store/images',verbose_name='Imagem',null=True,blank=True)
    description= models.TextField()
    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    bought = models.BooleanField(blank=True)

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('store:details',(),{'slug':self.slug})

    class Meta:
        verbose_name ='Produto'
        verbose_name_plural='Produtos'
        ordering =['name']


class Buy(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Usuario',
        related_name='buy'
    )
    product = models.ForeignKey(
        Product, verbose_name='Produto', related_name='buy'
    )
