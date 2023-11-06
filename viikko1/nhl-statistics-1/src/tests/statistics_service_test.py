import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_player(self):

        player = self.stats.search("Semenko")
        self.assertEqual(player.name,"Semenko")

    def test_search_notfound(self):

        player = self.stats.search("Pavel")
        self.assertIsNone(player)

    def test_search_by_team(self):
        
        result= self.stats.team("EDM")
        self.assertEqual(len(result),3)

    def test_sort_by_points(self):
        
        result = self.stats.top(2)
        self.assertEqual(len(result),2)
        

        

    

    





        