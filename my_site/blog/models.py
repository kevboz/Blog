from django.db import models
from django.core.validators import MinLengthValidator ,MaxLengthValidator


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    #image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts",null=True)
    post_date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    slug = models.SlugField(unique=True, db_index=True) # automatically does index.. don't really need db_index
    content = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(5000)])
    tags = models.ManyToManyField(Tag)

class Comment(models.Model):
    user_name =  models.CharField(max_length=120)
    user_email = models.EmailField()
    text =  models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")


    