# Create a project directory
mkdir myproject
cd myproject

# Create a new Django project
django-admin startproject mysite
cd mysite

# Create a new app within the project
python manage.py startapp books
# Production settings
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Database settings for production (example for PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'yourdbuser',
        'PASSWORD': 'yourdbpassword',
        'HOST': 'yourdbhost',
        'PORT': 'yourdbport',
    }
}
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
]
from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book': book})
<!DOCTYPE html>
<html>
<head>
    <title>Book List</title>
</head>
<body>
    <h1>Books</h1>
    <ul>
        {% for book in books %}
            <li><a href="{{ book.id }}/">{{ book.book_name }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name
python manage.py makemigrations
python manage.py migrate
from django.contrib import admin
from .models import Book

admin.site.register(Book)
python manage.py createsuperuser
python manage.py shell
from books.models import Book

# Create a new book
book = Book(book_name='1984', author='George Orwell', publisher='Secker & Warburg')
book.save()

# Retrieve all books
books = Book.objects.all()
print(books)
# Add 'books' to INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',
]

# Production settings example
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'yourdbuser',
        'PASSWORD': 'yourdbpassword',
        'HOST': 'yourdbhost',
        'PORT': 'yourdbport',
    }
}
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
]
from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book': book})
from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name
from django.contrib import admin
from .models import Book

admin.site.register(Book)
<!DOCTYPE html>
<html>
<head>
    <title>Book List</title>
</head>
<body>
    <h1>Books</h1>
    <ul>
        {% for book in books %}
            <li><a href="{{ book.id }}/">{{ book.book_name }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
