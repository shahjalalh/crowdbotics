# Crowdbotics #

## Requirements
- Django==1.10

## Install
In the terminal
```
$ virtualenv crowdboticsenv
$ source crowdboticsenv/bin/activate
(crowdboticsenv)$ cd crowdbotics
(crowdboticsenv)$ pip install -r requriements.txt
(crowdboticsenv)$ python manage.py migrate
(crowdboticsenv)$ python manage.py createsuperuser
(crowdboticsenv)$ python manage.py runserver

```

In Django Shell

```
$ python manage.py shell

>>> from users.models import User
>>> from dogs.models import Dog
>>> from cats.models import Cat

>>> user1 = User(username='atik', email='atik@gmail', password='atik_pass')
>>> user1.save()
>>> user1.username
>>> user1.first_name
>>> user1.first_name = 'Atik'
>>> user1.save()
>>> user1 = User.objects.filter(username='atik')
>>> user1.delete()

>>> user2 = User(username='arifin', email='arifin@email.com', password='arifin_pass')
>>> user2.save()
>>> user2.username
>>> user2.first_name
>>> user2.first_name = 'Arifin'
>>> user2.save()
>>> user2 = User.objects.filter(username='arifin')
>>> user2.delete()

>>> dog1 = Dog(name='tom', birthday='2017-10-04', owner=user1)
>>> dog1.save()
>>> dog1.name
>>> dog1.name = 'tomy'
>>> dog1.save()
>>> dog1 = Dog.objects.filter(name='tomy')
>>> dog1.delete()

>>> cat1 = Cat(name='mimi', birthday='2017-10-04', owner=user2)
>>> cat1.save()
>>> cat1.name
>>> cat1.name = 'lion'
>>> cat1.save()
>>> cat1 = Cat.objects.filter(name='lion')
>>> cat1.delete()

>>> User.objects.all()

>>> Dog.objects.all()

>>> Cat.objects.all()

>>> Dog.objects.filter(owner=user1)

>>> Cat.objects.filter(owner=user2)

```