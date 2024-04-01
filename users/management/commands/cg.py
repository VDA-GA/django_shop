from django.core.management import BaseCommand

from users.models import User

from django.contrib.auth.models import Group


class Command(BaseCommand):

    def handle(self, *args, **options):
        group = Group.objects.create(
            name='Moderators',
        )
        group.save()
        user = User.objects.get(email='test@mail.ru')
        g = Group.objects.get(name='Moderators')
        user.groups.add(g)
        user.save()
