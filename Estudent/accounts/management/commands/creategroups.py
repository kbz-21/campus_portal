from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create default role groups'

    def handle(self, *args, **options):
        roles = ['Admin', 'Teacher', 'Student', 'Parent']
        for role in roles:
            Group.objects.get_or_create(name=role)
        self.stdout.write(self.style.SUCCESS(f'Successfully created roles: {", ".join(roles)}'))