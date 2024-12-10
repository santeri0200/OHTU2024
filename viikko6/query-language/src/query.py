from matchers import All, And, Or, Not, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self, command=All()):
        self.command = command

    def build(self):
        return self.command

    def one_of(self, *matchers):
        return QueryBuilder(And(self.command, Or(*matchers)))

    def plays_in(self, team):
        return QueryBuilder(And(self.command, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.command, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.command, HasFewerThan(value, attr)))
