from model_bakery.recipe import Recipe

from ..models import ProgrammingLanguage

user_recipe = Recipe("User", username="testing")

python_recipe = Recipe(
    "me.ProgrammingLanguage", user=user_recipe, name=ProgrammingLanguage.PYTHON
)

javascript_recipe = Recipe(
    "me.ProgrammingLanguage", user=user_recipe, name=ProgrammingLanguage.JAVASCRIPT
)

elixir_recipe = Recipe(
    "me.ProgrammingLanguage", user=user_recipe, name=ProgrammingLanguage.ELIXIR
)
