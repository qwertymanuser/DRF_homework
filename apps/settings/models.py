from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=230,
        verbose_name="Название сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to="logo_image/",
        verbose_name="Логотип сайта"    
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Номер телефона"
    )
    banner = models.ImageField(
        upload_to="banner_image/",
        verbose_name="Логотип сайта"  
     
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    adress = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки сайт"
        verbose_name_plural = "Настройка сата" 

class BlogDetail(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="описание"
    )
    # image = models.ImageField(
    #     upload_to="about_image/",
    #     verbose_name="Фотография"
#     )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Blog_detail"
        verbose_name_plural  = "Blog_detaili"

class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Вход",
    )

    descriptions = models.TextField(
        verbose_name="описание"
    )
    image = models.ImageField(
        upload_to="academics_image/",
        verbose_name="Фотография"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog" 
    

class BooksDetail(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Вход",
    )

    descriptions = models.TextField(
        verbose_name="описание"
    )
    image = models.ImageField(
        upload_to="blog-post_image/",
        verbose_name="Фотография"
    )
    
    def __str__(self):
        return self.title
    

class Books(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Вход",
    )

    descriptions = models.TextField(
        verbose_name="описание"
    )
    image = models.ImageField(
        upload_to="research_image/",
        verbose_name="Фотография"
    )
    def __str__(self):
        return self.title   
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги" 
    
class Image(models.Model):
    category_name = models.CharField(
        max_length=50
    )

    image = models.ImageField(
        upload_to="imagee/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return self.title   
    

class Contact(models.Model):
    number = models.CharField(
        max_length=50
    )
    email = models.EmailField(
    verbose_name="Email"
    )
    def __str__(self):
        return self.title  
    
    