from django.db import models

# Create your models here.
# will inherit model and then from models u inherit a class called Model

CATEGORIES = (
    {
        ('Politics', 'Politics'),
        ('Technology', 'Technology'),
        ('Education', 'Education'),
        ('Science', 'Science'),
        ('History', 'History'),
        ('Fiction', 'Fiction')
    }
)

# C:\Users\USER\PycharmProjects\DjangoProject\Vetix_db\db.sqlite3
class Book(models.Model):
    # CREATING THE COLUMNS for the table in database
    title = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORIES, max_length=200)
    year = models.IntegerField()
    cost = models.IntegerField()
    isbn = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    #  a class that has more information
    class Meta:
        db_table = 'Books'  # i want my table to be called Books

#  COMMAND FOR CREATING A Table also when adding something on the fields
#     python manage.py makemigrations
#     python manage.py migrate
