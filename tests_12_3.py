import unittest

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


def skip_if_frozen(test_func):
    def wrapper(self):
        if self.is_frozen:
            print('Тесты в этом кейсе заморожены')
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_func(self)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

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

    @skip_if_frozen
    def test_walk(self):
        self.runner1.walk()
        self.assertEqual(self.runner1.distance, 5)

    @skip_if_frozen
    def test_run(self):
        self.runner1.run()
        self.assertEqual(self.runner1.distance, 10)

    @skip_if_frozen
    def test_challenge(self):
        self.assertNotEqual(self.runner1, self.runner2)


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        results = tournament.start()
        self.all_results[1] = results
        self.assertEqual(results[max(results)], "Ник")

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        results = tournament.start()
        self.all_results[2] = results
        self.assertEqual(results[max(results)], "Ник")

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        results = tournament.start()
        self.all_results[3] = results
        self.assertEqual(results[max(results)], "Ник")


if __name__ == '__main__':
    # Создание тестового набора
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    # Запуск тестового набора
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)