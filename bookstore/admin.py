
from django.contrib import admin

from .models import Author, Book, Publisher, Store


class BookInlineModelAdmin(admin.TabularInline):
    model = Book


class PublisherInlineModelAdmin(admin.TabularInline):
    model = Publisher


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "country"]
    fields = ['name', 'surname', "country"]
    search_fields = ["surname"]
    inlines = [BookInlineModelAdmin]


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'author']
    fields = ['title', 'pubdate', 'author', 'publisher', ('price', 'pages')]
    raw_id_fields = ['author', ]
    date_hierarchy = "pubdate"
    list_filter = ['price', 'pubdate']
    filter_vertical = ["publisher"]
    search_fields = ["author", "title"]


@admin.register(Store)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ["name", "address"]
    fields = ['name', 'address']
    search_fields = ["name", "address"]
    inlines = [PublisherInlineModelAdmin]


@admin.register(Publisher)
class PublisherModelAdmin(admin.ModelAdmin):
    list_display = ["name", "store"]
    fields = ['name', "year", 'store']
    search_fields = ["name", "store"]
