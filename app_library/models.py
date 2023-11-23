from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    author = models.CharField(max_length=250, db_index=True)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
