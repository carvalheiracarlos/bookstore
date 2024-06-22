from django.db import models
from django.core.validators import MinValueValidator


from core.validators import year_validator
from core.models import BaseModel

       
class BookCategory(BaseModel):
    name = models.CharField('Nome da categoria', max_length=255)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class BookAuthor(BaseModel):
    name = models.CharField('Nome do Autor', max_length=255)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name

class Book(BaseModel):
    title = models.CharField('Título', max_length=255)
    release_year = models.PositiveSmallIntegerField('Ano de lançamento', null=True, blank=True, validators=[year_validator])
    quantity = models.PositiveSmallIntegerField('Quantidade de Livros em Estoque', validators=[MinValueValidator(0)])
    author = models.ForeignKey(BookAuthor, verbose_name='Autor do Livro', on_delete=models.CASCADE)
    category = models.ForeignKey(BookCategory, verbose_name='Categoria do Livro', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ('-created',)

    def __str__(self):
        return self.title
 