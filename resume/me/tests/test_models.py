"""Test models"""

import pytest
from model_bakery import baker

from ..models import ProgrammingLanguage
from .recipes import user_recipe


@pytest.mark.django_db
def test_programming_language__elixir_choice():
    user = baker.make("User")
    language = ProgrammingLanguage(user=user, name=ProgrammingLanguage.ELIXIR)
    language.save()

    assert language.get_name_display() == "Elixir"


@pytest.mark.django_db
def test_programming_language__str():
    user = user_recipe.make()
    language = ProgrammingLanguage(user=user, name=ProgrammingLanguage.ELIXIR)
    language.save()

    assert str(language) == "Elixir - @testing"
