"""Test views for me app"""

import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertContains

from .recipes import elixir_recipe, javascript_recipe, python_recipe, user_recipe


@pytest.mark.django_db
def test_landing_page(client: Client):
    user_recipe.make(username="supertesting")
    url = reverse("me:home")
    profile_url = reverse("me:profile", args=["supertesting"])

    response = client.get(url)

    assertContains(response, "@supertesting")
    assertContains(response, profile_url)


@pytest.mark.django_db
def test_profile_view(client: Client):
    user = user_recipe.make(username="tester")
    python_recipe.make(user=user)
    javascript_recipe.make(user=user)
    elixir_recipe.make(user=user)
    url = reverse("me:profile", args=[user.username])

    response = client.get(url)

    assertContains(response, "Perfil de @tester")
    assertContains(response, "Python")
    assertContains(response, "JavaScript")
    assertContains(response, "Elixir")
