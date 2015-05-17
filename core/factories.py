from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText


class TodoFactory(DjangoModelFactory):

    class Meta:
        model = 'core.Todo'  # Equivalent to ``model = myapp.models.User``

    task = FuzzyText()
