from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import ReviewModel, SightModel


User = get_user_model()


class UserTest(TestCase):
    def test_create_user(self):
        User.objects.create(username="ivan_99", email="ivan@example.com", password="Standard_Pass123")
        User.objects.create(username="user_caps", email="USER@EXAMPLE.COM", password="ValidPass!")
        User.objects.create(username="a", email="a@b.cc", password="Short1")
        User.objects.create(username="юзер_кириллица", email="тест@домен.рф", password="Password123")
        User.objects.create(username="alex-cool", email="alex.cool@domain.co.uk", password="Safe_P@ss")
        User.objects.create(username="sql_inj' OR '1'='1", email="admin@system.com", password="VeryComplex_Pass_2026!")
        User.objects.create(username="duplicate_user", email="unique1@example.com", password="SomePassword1")
        User.objects.create(username="another_user", email="unique2@example.com", password="Password50Symbols")
        User.objects.create(username="user.with.dots", email="dots@example.com", password="Password_2026")
        User.objects.create(username="spaced_user", email="space@example.com", password="Spaces123")
        User.objects.create(username="A" * 10000, email="overflow@example.com", password="NormalPassword1")
        User.objects.create(username="null_byte\x00user", email="null@example.com", password="NormalPassword2")
        User.objects.create(username="drop_table", email="admin@system.com", password="'); DROP TABLE auth_user; --")
        User.objects.create(username="emoji_𓂺_💥", email="💥@💥.💥", password="NormalPassword4")
        User.objects.create(username="   ", email="   @   .   ", password="               ")

    def test_get_user(self):
        user_1 = User.objects.filter(username="ivan_99").first()