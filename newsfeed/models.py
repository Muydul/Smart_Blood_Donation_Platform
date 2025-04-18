from django.db import models
from profiles.models import Aprofile, bloodGroup

statusType = (

    ('Emergency', 'Emergency'),
    ('Managed', 'Managed'),
)


class Arequest(models.Model):
    title = models.CharField(max_length=200,editable=False)
    description = models.TextField()
    author = models.ForeignKey(Aprofile, on_delete=models.CASCADE)
    reqForDonate = models.ManyToManyField(
        Aprofile, default=None, related_name='requestForDonate', blank=True)

    bloodGroup = models.CharField(
        max_length=3, default="A+", choices=bloodGroup)
    location = models.CharField(max_length=100,default="Dhaka Medical Hospital")
    bag = models.IntegerField(default=1)
    type = models.CharField(
        max_length=10, choices=statusType, default="Emergency")
    phoneNum = models.BigIntegerField(default=880)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def CommentCount(self):
        return self.comment_set.all().count()

    def save(self, *args, **kwargs):
        self.title = f'{self.author.user.username} needs {self.bloodGroup}' 
        super(Arequest, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    user = models.ForeignKey(Aprofile, on_delete=models.CASCADE)
    post = models.ForeignKey(Arequest, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


