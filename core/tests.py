from django.test import TestCase
from django.test import Client

from nose.tools import assert_equals

from .factories import TodoFactory
from .models import Todo


class TodoTest(TestCase):

    def setUp(self):
        count = 0
        while (count < 12):
            TodoFactory()
            count += 1

    def test_list(self):
        c = Client()

        # test if paginate by 10
        response = c.get('/')
        assert_equals(response.context['todos'].count(), 10)

        response = c.get('/?page=2')
        assert_equals(response.context['todos'].count(), 2)

        # Test ORM and if we have to 12 elements pending and
        assert_equals(Todo.objects.pending().count(), 12)
        assert_equals(Todo.objects.done().count(), 0)

    def test_create(self):
        c = Client()

        c.post('/create/', {'task': 'lorem ipsum'})

        # should be there 3 task in second page
        response = c.get('/?page=2')
        assert_equals(response.context['todos'].count(), 3)

        # Test ORM and if we have to 12 elements pending and
        assert_equals(Todo.objects.pending().count(), 13)
        assert_equals(Todo.objects.done().count(), 0)

    def test_delete(self):
        c = Client()

        # we will delete 2 elements first and last
        first = Todo.objects.first()
        last = Todo.objects.last()

        c.post('/delete/%s/' % first.id)
        c.post('/delete/%s/' % last.id)

        response = c.get('/')
        assert_equals(response.context['todos'].count(), 10)

        assert_equals(Todo.objects.pending().count(), 10)
        assert_equals(Todo.objects.done().count(), 0)

    def test_done(self):
        c = Client()

        # we will delete 2 elements first and last
        first = Todo.objects.first()
        last = Todo.objects.last()

        c.post('/toggle/%s/' % first.id)
        c.post('/toggle/%s/' % last.id)

        assert_equals(Todo.objects.pending().count(), 10)
        assert_equals(Todo.objects.done().count(), 2)

        # revert one task
        c.post('/toggle/%s/' % last.id)
        assert_equals(Todo.objects.pending().count(), 11)
        assert_equals(Todo.objects.done().count(), 1)
