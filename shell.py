import datetime
from user.models import Student, Mentor, Language, Course

l1 = Language.objects.create(
    name='Python',
    months_to_learn=6
)
print(l1)

l2 = Language.objects.create(
    name='JavaScript',
    months_to_learn=6
)
print(l2)

l3 = Language.objects.create(
    name='UX-UI',
    months_to_learn=2
)
print(l3)

s1 = Student.objects.create(
    name='Amanov Aman',
    email='aman@mail.ru',
    phone_number='+996700989898',
    work_study_place='School №13',
    has_own_notebook=True,
    preferred_os='windows'
)
print(s1)

s2 = Student.objects.create(
    name='Apina Alena',
    email='aapina@bk.ru',
    phone_number='0550888888',
    work_study_place='TV',
    has_own_notebook=True,
    preferred_os='mac'
)
print(s2)

s3 = Student.objects.create(
    name='Phil Spencer',
    email= 'spencer@microsoft.com',
    phone_number='0508312312',
    work_study_place='Microsoft Gaming',
    has_own_notebook=False,
    preferred_os='linux'
)
print(s3)

m1 = Mentor.objects.create(
    name='Ilona Maskova',
    email='imask@gmail.com',
    phone_number='0500545454',
    main_work=None,
    experience='2021-10-23'
)
print(m1)

m2 = Mentor.objects.create(
    name='Halil Nurmuhametov',
    email='halil@gmail.com',
    phone_number='0709989876',
    main_work='University of Fort Collins',
    experience='2010-09-18'
)
print(m2)


c1 = Course.objects.create(
    name='Python-21',
    language=l1,
    mentor=m2,
    student=(s1, s2),
    date_started='2022-01-08'
)
print(c1)

c2 = Course.objects.create(
    name='UX-UI design',
    language=l3,
    mentor=m1,
    student=s3,
    date_started='2022-22-08'
)
print(c2)

c = Course.objecrs.all()
print(c)