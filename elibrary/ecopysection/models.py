from django.db import models

# Create your models here.


class ECopies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    department_choices = (
        ('Biotechnology', 'Biotechnology'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Computer Science & Engineering', 'Computer Science & Engineering'),
        ('Chemistry', 'Chemistry'),
        ('Electronics & Communication Engineering', 'Electronics & Communication Engineering'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Earth & Environmental Studies', 'Earth & Environmental Studies'),
        ('Humanities & Social Sciences', 'Humanities & Social Sciences'),
        ('Mathematics', 'Mathematics'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Metallurgical & Materials Engineering', 'Metallurgical & Materials Engineering'),
        ('Management Studies', 'Management Studies'),
        ('Physics', 'Physics'),
    )
    department = models.CharField(max_length=100, choices=department_choices, blank=True, null=True)
    type_choices = (
        ('Course Book', 'Course Book'),
        ('Reference Book', 'Reference Book'),
        ('Others', 'Others'),
    )
    type = models.CharField(max_length=100, choices=department_choices, blank=True, null=True)
    external_link = models.URLField()
    # TODO
    # AUTOGENERATE DATETIME
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_cname(self):
        class_name = "E-Copy"
        return class_name

    class Meta:
        managed = True
        ordering = ['-created_at']
        db_table = 'ecopies'
        verbose_name_plural = 'E-Copies'
