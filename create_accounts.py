
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop_portal.settings')
django.setup()

from django.contrib.auth.models import User, Group
from workshop_app.models import Profile

def create_user(username, password, email, first_name, last_name, position):
    user, created = User.objects.get_or_create(username=username, email=email)
    if created:
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        print(f"User {username} created.")
    else:
        print(f"User {username} already exists.")

    profile, p_created = Profile.objects.get_or_create(user=user)
    profile.position = position
    profile.institute = "Test Institute"
    profile.department = "computer engineering"
    profile.phone_number = "9999999999"
    profile.is_email_verified = True  # Verify so they can login
    profile.save()
    print(f"Profile for {username} updated/created.")

    if position == 'instructor':
        group, g_created = Group.objects.get_or_create(name='instructor')
        user.groups.add(group)
        print(f"User {username} added to instructor group.")

if __name__ == "__main__":
    create_user("coordinator1", "password123", "coordinator1@example.com", "Test", "Coordinator", "coordinator")
    create_user("instructor1", "password123", "instructor1@example.com", "Test", "Instructor", "instructor")
