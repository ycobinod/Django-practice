from django.db import models

#for publisher
class Publisher(models.Model) :
    name=models.CharField( max_length=50,help_text="the name of the publisher" )
    website=models.URLField(help_text="the website of the publisher")
    email=models.EmailField(help_text="the email of the publisher")

    def __str__(self):
        return self.name
#for Book  
class Book(models.Model):
    title=models.CharField(max_length=50,help_text="the title of the book")
    publication_date=models.DateField(verbose_name="date the book was published")
    isbn=models.CharField(max_length=50,verbose_name="the isbn number of books")
    
#for contributors
class Contributor(models.Model):
    first_name=models.CharField(max_length=20,help_text="first name of the contributors")
    last_name=models.CharField(max_length=20,help_text="last name of the contributors")
    email=models.EmailField(max_length=254,help_text="email of the contributors")


        



    
