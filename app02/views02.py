from django.shortcuts import render
from django.http import HttpResponse
from app02 import models


def add_book(request):
    pass
    # #  获取出版社对象
    # pub_obj = models.Publish.objects.filter(pk=1).first()
    # #  给书籍的出版社属性publish传出版社对象
    # book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
    # print(book, type(book))
    # return HttpResponse(book)

    # #  获取出版社对象
    # pub_obj = models.Publish.objects.filter(pk=1).first()
    # #  获取出版社对象的id
    # pk = pub_obj.pk
    # #  给书籍的关联出版社字段 publish_id 传出版社对象的id
    # book = models.Book.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)
    # print(book, type(book))
    # return HttpResponse(book)

    # #  获取作者对象
    # chong = models.Author.objects.filter(name="令狐冲").first()
    # ying = models.Author.objects.filter(name="任盈盈").first()
    # #  获取书籍对象
    # book = models.Book.objects.filter(title="菜鸟教程").first()
    # #  给书籍对象的 authors 属性用 add 方法传作者对象
    # book.authors.add(chong, ying)
    # return HttpResponse(book)

    # #  获取作者对象
    # chong = models.Author.objects.filter(name="令狐冲").first()
    # #  获取作者对象的id
    # pk = chong.pk
    # #  获取书籍对象
    # book = models.Book.objects.filter(title="冲灵剑法").first()
    # #  给书籍对象的 authors 属性用 add 方法传作者对象的id
    # book.authors.add(pk)








