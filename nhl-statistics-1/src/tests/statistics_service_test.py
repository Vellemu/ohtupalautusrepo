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
        
    def test_search(self):
        found = self.stats.search("Kurri")
        self.assertEqual(found.name, "Kurri")
        self.assertEqual(found.team, "EDM")
        self.assertEqual(found.goals, 37)
        self.assertEqual(found.assists, 53)
    
    def test_search_not_in_list(self):
        found = self.stats.search("Koivu")
        self.assertEqual(found, None)
            
    def test_team(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)
    
    def test_team_no_players(self):
        team = self.stats.team("Tappara")
        self.assertEqual(len(team), 0)
    
    def test_top(self):
        top = self.stats.top(2)
        self.assertEqual(len(top), 3)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")
    
    def test_top_out_of_top_three(self):
        top = self.stats.top(2)
        self.assertEqual(len(top), 3)
        top_names = [player.name for player in top]
        self.assertNotIn("Kurri", top_names)