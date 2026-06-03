from dataclasses import dataclass
from uuid import uuid4

from faker import Faker


fake = Faker()


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    password: str


def random_user():
    return User(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=f"qa_{uuid4().hex}@gmail.com",
        password="Password123!",
    )


invalid_user = User(
    first_name="Invalid",
    last_name="User",
    email="wrong_user@example.com",
    password="wrong_password",
)


registered_user = User(
    first_name="Test",
    last_name="User",
    email="testuserqa123@gmail.com",
    password="Password123!",
)