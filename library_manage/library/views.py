from django.shortcuts import render, HttpResponse, redirect
from library import models


def index(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")


def publisher_list(request):
    ret = models.Publisher.objects.all()
    print(ret)
    # ret = models.Publisher.objects.all().order_by("id")
    return render(request, "publisher/publisher_list.html", {"publisher_list": ret})


def add_publisher(request):
    if request.method == "POST":
        new_name = request.POST.get("publisher_name")

        models.Publisher.objects.create(name=new_name)
        return redirect("/publisher_list/")

    return render(request, "publisher/add_publisher.html")


def delete_publisher(request):
    error_msg = ""
    del_id = request.GET.get('id', None)
    if del_id:
        del_obj = models.Publisher.objects.get(id=del_id).delete()
        return redirect("/publisher_list/")

    else:
        error_msg = "删除的id不存在!"

    return render(request, "publisher/add_publisher.html", {"error": error_msg})


def edit_publisher(request):
    if request.method == "POST":
        new_name = request.POST.get('publisher_name')
        edit_id = request.POST.get('id')
        edit_obj = models.Publisher.objects.get(id=edit_id)
        edit_obj.name = new_name
        edit_obj.save()

        return redirect("/publisher_list/")

    edit_id = request.GET.get('id')
    if edit_id:
        edit_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "publisher/edit_publisher.html", {"publisher": edit_obj})


def book_list(request):
    all_book = models.Book.objects.all()
    # print(all_book)
    return render(request, "book/book_list.html", {"book_list": all_book})


def add_book(request):
    if request.method == "POST":
        new_book = request.POST.get("book_name")
        new_publisher = request.POST.get("publisher")

        models.Book.objects.create(title=new_book, publisher_id=new_publisher)
        return redirect("/book_list/")
    ret = models.Publisher.objects.all()
    return render(request, "book/add_book.html", {"publisher_list": ret})


def edit_book(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_title = request.POST.get("title")
        new_publisher = request.POST.get("publisher")

        edit_obj = models.Book.objects.get(id=edit_id)
        edit_obj.title = new_title
        edit_obj.publisher_id = new_publisher
        edit_obj.save()

        return redirect("/book_list/")

    edit_id = request.GET.get("id")
    edit_book_obj = models.Book.objects.get(id=edit_id)
    ret = models.Publisher.objects.all()
    return render(request, "book/edit_book.html", {"publisher_list": ret, "book": edit_book_obj})


def delete_book(request):
    del_id = request.GET.get("id")
    if del_id:
        models.Book.objects.get(id=del_id).delete()

    return redirect("/book_list/")


def author_list(request):
    ret = models.Author.objects.all()

    return render(request, "author/author_list.html", {"author_list": ret})


def add_author(request):
    if request.method == "POST":
        new_name = request.POST.get("name")
        books = request.POST.getlist("books")
        new_author_obj = models.Author.objects.create(name=new_name)

        new_author_obj.book.set(books)

        return redirect("/author_list/")

    ret = models.Book.objects.all()
    return render(request, "author/add_author.html", {"book_list": ret})


def edit_author(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_name = request.POST.get("author")
        books = request.POST.getlist("books")
        edit_obj = models.Author.objects.get(id=edit_id)
        edit_obj.name = new_name
        edit_obj.book.set(books)
        edit_obj.save()
        return redirect("/author_list/")

    edit_id = request.GET.get("id")
    author_ret = models.Author.objects.get(id=edit_id)
    book_ret = models.Book.objects.all()

    return render(request, "author/edit_author.html", {"author": author_ret, "book_list": book_ret})


def delete_author(request):
    del_id = request.GET.get("id")
    if del_id:
        models.Author.objects.get(id=del_id).delete()

    return redirect("/author_list/")


