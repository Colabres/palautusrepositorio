

# class OneOf:
#     def __init__(self, m1, m2):
#         self._m1 = m1
#         self._m2 = m2
#         print(f"OneOf initialized with m1:{m1} , m2: ")
        
#     def test(self, player):
#         print("Testing OneOf")
#         return self._m1.test(player) or self._m2.test(player)

class All:
    

    def test(self, player):

        return True


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False



class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)



class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._matcher=Not(HasAtLeast(value,attr))

    def test(self, player):
        
        return self._matcher.test(player)



class QueryBuilder:
    def __init__(self,query=All()):
        #self._matchers = []
        self._query=query

    def oneOf(self,m1,m2):
        #self._matchers.append(Or(m1,m2))
        #self._matchers.append(OneOf(m1,m2))
        #print(self._matchers)

        return QueryBuilder(Or(m1,m2))


    def playsIn(self, team):
        #self._matchers.append(PlaysIn(team))
        return QueryBuilder(And(self._query,PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        #self._matchers.append(HasAtLeast(value, attr))
        return QueryBuilder(And(self._query,HasAtLeast(value,attr)))

    def hasFewerThan(self, value, attr):
        #self._matchers.append(HasFewerThan(value, attr))
        return QueryBuilder(And(self._query,HasFewerThan(value,attr)))

    
    def build(self):
        return self._query
