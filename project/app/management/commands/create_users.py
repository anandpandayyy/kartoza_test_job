from app.models import User
from django.core.management.base import BaseCommand
import json
from django.db.utils import IntegrityError


class Command(BaseCommand):
    """
    Creating user from json file
    """

    def handle(self, *args, **kwargs):
        try:
            with open("app/user_data.json") as json_file:
                data = json.load(json_file)
                User.objects.create_superuser(
                    username=data["client"][0]["username"],
                    email=data["client"][0]["email"],
                    password=data["client"][0]["password"],
                    lon=data["client"][0]["lon"],
                    lat=data["client"][0]["lat"],
                )
                for new in data["client"][1:]:
                    User.objects.create_user(
                        username=new["username"],
                        email=new["email"],
                        password=new["password"],
                        lon=new["lon"],
                        lat=new["lat"],
                    )
                print("User's created successfully")
        except IntegrityError:
            print("Managment command already runned successfully")
