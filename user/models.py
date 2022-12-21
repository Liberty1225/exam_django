from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=20)
    month_to_learn = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class AbstractPerson(models.Model):
    name = models.CharField(max_length=20, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Электронная почта")
    phone_number = models.CharField(max_length=13, verbose_name="Номер телефона")

    def __str__(self):
        return self.name
    #
    # def save(self, *args, **kwargs):
    #     if self.phone_number[0] == '0':
    #         self.phone_number[0] == '+996'
    #     super().save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['name', ]


OS_CHOICES = (
    ('windows', 'Windows'),
    ('macos', 'MacOS'),
    ('linux', 'Linux'),
)


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=30, null=True, blank=True)
    has_own_notebook = models.BooleanField(default=False)
    preferred_os = models.CharField(max_length=30, choices=OS_CHOICES)

    class Meta(AbstractPerson.Meta):
        pass


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=30, null=True, blank=True, verbose_name="Основное место работы")
    experience = models.DateField(verbose_name="Дата рождения")
    study = models.ManyToManyField(Student, related_name="studies", through='Course')

    def __str__(self):
        return self.main_work


class Course(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Название курса")
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_started = models.DateField()

    def __str__(self):
        return f'{self.language.name}'

