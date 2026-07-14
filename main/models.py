from django.db import models


class Project(models.Model):

    title = models.CharField(
        max_length=100
    )


    description = models.TextField()


    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )


    github_link = models.URLField(
        blank=True
    )


    demo_link = models.URLField(
        blank=True
    )


    technologies = models.CharField(
        max_length=200,
        blank=True,
        help_text="مثال: Python, Django, HTML, CSS"
    )


    created_at = models.DateField(
        auto_now_add=True
    )


    def __str__(self):

        return self.title





class ContactMessage(models.Model):

    name = models.CharField(
        max_length=100
    )


    email = models.EmailField()


    message = models.TextField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.name