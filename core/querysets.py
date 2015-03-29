from django.db.models import QuerySet


class TodoQuerySet(QuerySet):

    def done(self):
        return self.filter(done=True)

    def pending(self):
        return self.filter(done=False)
