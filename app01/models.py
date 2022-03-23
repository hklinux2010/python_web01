from django.db import models


# Create your models here.


class Test(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=20)


class Test2(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class add(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=40)


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()
