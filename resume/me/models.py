"""Me app models"""

from django.contrib.auth import get_user_model
from django.db import models
from model_utils.models import TimeStampedModel

User = get_user_model()


class ProgrammingLanguage(TimeStampedModel):
    """Programming language model"""

    PYTHON = 0
    JAVASCRIPT = 1
    JAVA = 2
    C = 3
    CPP = 4
    CSHARP = 5
    PHP = 6
    GO = 7
    RUST = 8
    DART = 9
    ELIXIR = 10
    NAME_CHOICES = [
        (PYTHON, "Python"),
        (JAVASCRIPT, "JavaScript"),
        (JAVA, "Java"),
        (C, "C"),
        (CPP, "C++"),
        (CSHARP, "C#"),
        (PHP, "PHP"),
        (GO, "Go"),
        (RUST, "Rust"),
        (DART, "Dart"),
        (ELIXIR, "Elixir"),
    ]
    name = models.PositiveSmallIntegerField(choices=NAME_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.get_name_display()} - @{self.user.username}"
