from django.db import models

CITY_CHOICES = [
    ('osh', 'Ош'),
    ('bishkek', 'Бишкек'),
    ('manas', 'Манас'),
    ('batken', 'Баткен'),
    ('talas', 'Талас'),
]

class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    city = models.CharField(max_length=20, choices=CITY_CHOICES)
    address = models.CharField(max_length=255)
    medical_info = models.TextField(max_length=2000)

    def str(self):
        return f"{self.first_name[0]}. {self.last_name} ({self.birth_date})"
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.post.title}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like on {self.post.title}"
