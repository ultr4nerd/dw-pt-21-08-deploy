"""Me app views"""

from typing import Any

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

User = get_user_model()


class HomeView(TemplateView):
    """Home view"""

    template_name = "me/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context


class ProfileView(TemplateView):
    """Profile view"""

    template_name = "me/profile.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get("username")
        user = get_object_or_404(User, username=username)
        context["user"] = user
        context["languages"] = user.programminglanguage_set.all()
        return context
