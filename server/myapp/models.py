from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)

    def __str__(self):
        max_length = 6
        if len(self.name) > max_length:
            return self.name[:max_length] + "..."
        else:
            return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        max_length = 6
        if len(self.name) > max_length:
            return self.name[:max_length] + "..."
        else:
            return self.name

class Note(models.Model):
    description = models.CharField(max_length=1000)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        max_length = 6
        if len(self.description) > max_length:
            return self.description[:max_length] + "..."
        else:
            return self.description
