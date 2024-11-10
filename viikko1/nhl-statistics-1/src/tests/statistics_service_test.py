import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  # 16
            Player("Lemieux", "PIT", 45, 54), # 99
            Player("Kurri",   "EDM", 37, 53), # 90
            Player("Yzerman", "DET", 42, 56), # 98
            Player("Gretzky", "EDM", 35, 89)  # 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_hae_pelaajaa(self):
        stub = PlayerReaderStub()
        for player in stub.get_players():
            self.assertEquals(self.stats.search(player.name), player)

        self.assertEqual(self.stats.search("NonExisting"), None)

    def test_hae_joukkue(self):
        for player in self.stats._players:
            self.assertEqual(self.stats.team(player.team), [other for other in self.stats._players if other.team == player.team])

        self.assertEqual(self.stats.team("NonExisting"), [])

    def test_top_pelaaja(self):
        method = SortBy.POINTS
        for i in range(1, len(self.stats._players)):
            top_players = self.stats.top(i, method)
            self.assertEqual(len(top_players), i)
            self.assertEqual([player.name for player in top_players], ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"][:i])

        method = SortBy.GOALS
        for i in range(1, len(self.stats._players)):
            top_players = self.stats.top(i, method)
            self.assertEqual(len(top_players), i)
            self.assertEqual([player.name for player in top_players], ["Lemieux", "Yzerman", "Kurri", "Gretzky", "Semenko"][:i])

        method = SortBy.ASSISTS
        for i in range(1, len(self.stats._players)):
            top_players = self.stats.top(i, method)
            self.assertEqual(len(top_players), i)
            self.assertEqual([player.name for player in top_players], ["Gretzky", "Yzerman", "Lemieux", "Kurri", "Semenko"][:i])
