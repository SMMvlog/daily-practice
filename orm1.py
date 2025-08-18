# students = Student.objects.all() 
# for student in students: 
#       print (student) 
 
# #2 .  
# for student in Student.objects.all(): 
#       print (student) 




	

# fetch all titles of books written by a particular author

# from django.db import models 
# class Author(models.Model):
#        name = models.CharField(max_length=100)
 
# class Book(models.Model):
# title = models.CharField(max_length=200)
# author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

# Author.objects.annotate("name").values("title")


# for author in Book.objects.select_related("author"):
#        print(f"{author.author.name} == {author.title}")