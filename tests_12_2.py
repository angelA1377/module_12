class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def walk(self):
        self.distance += self.speed * 0.5

    def run(self):
        self.distance += self.speed

    def __eq__(self, other):
        return self.name == other.name


class Tournament:
    def __init__(self, distance, participants):
        self.distance = distance
        self.participants = participants

    def start(self):
        results = {}
        for runner in self.participants:
            time = self.distance / runner.speed
            results[time] = runner.name
        return {k: results[k] for k in sorted(results)}

import unittest

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_tournament_usain_nick(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        results = tournament.start()
        self.all_results[1] = results
        self.assertEqual(results[max(results)], "Ник")

    def test_tournament_andrey_nick(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        results = tournament.start()
        self.all_results[2] = results
        self.assertEqual(results[max(results)], "Ник")

    def test_tournament_usain_andrey_nick(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        results = tournament.start()
        self.all_results[3] = results
        self.assertEqual(results[max(results)], "Ник")

# Запуск тестов
if __name__ == '__main__':
    unittest.main()