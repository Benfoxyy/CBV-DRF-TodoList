from django.db import models

class ToDoList(models.Model):
    author = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content