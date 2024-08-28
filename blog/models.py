from django.db import models

class Post(models.Model):
    # данные о записи:
    title = models.CharField('Заголовок', max_length = 75)
    description = models.TextField('Текст')
    author = models.CharField('Имя автора', max_length = 50)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изоброжение', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Записи'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    #Комментарии
    email = models.EmailField()
    name = models.CharField('Имя', max_length = 50)
    text_comment = models.TextField('Текст комментария', max_length = 2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'

class Likes(models.Model):
    #лайки
    ip = models.CharField('IP-адрес', max_length = 100)
    post = models.ForeignKey(Post, verbose_name='Публикацыя', on_delete = models.CASCADE)
