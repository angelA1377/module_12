import unittest
from Runner_12_4 import Runner, Tournament
import logging

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8',
                        format='%(asctime)s | %(funcName)s | %(module)s | %(levelname)s: %(message)s')

class RunnerTest(unittest.TestCase):



    def test_run(self):
        try:
            runner = Runner(3, 5)

            runner.run()
            logging.info('"test_run" выполнен успешно')


        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")


    def test_walk(self):
        try:
            runner = Runner('ggg', -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')


        except ValueError:
            logging.warning('Неверная скорость для Runner')




    def test_challenge(self):
        runner1 = Runner('Igor')
        runner2 = Runner('Yulia')

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.part_1 = Runner('Усэйн', speed=4)
        self.part_2 = Runner('Андрей', speed=10)
        self.part_3 = Runner('Ник', speed=2)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        self.tournament_1 = Tournament(90, self.part_1, self.part_3)  # создаем объект класса Забег
        self.all_results = self.tournament_1.start()  # в словарь all_result записываем результат функции (место:участн)
        last_runner_name = self.all_results[
            max(self.all_results.keys())].name  # записываем имя с максимальным местом
        self.assertTrue(last_runner_name == 'Ник')  # вызываем юнит-метод сравнения
        TournamentTest.all_results[1] = self.all_results  # записываем словарь с ключом 1

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        self.tournament_2 = Tournament(90, self.part_2, self.part_3)  # создаем объект класса Забег
        self.all_results = self.tournament_2.start()  # в словарь all_result записываем результат функции (место:участн)
        last_runner_name = self.all_results[
            max(self.all_results.keys())].name  # записываем имя с максимальным местом
        self.assertTrue(last_runner_name == 'Ник')  # вызываем юнит-метод сравнения
        TournamentTest.all_results[2] = self.all_results  # записываем словарь с ключом 2

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):

        self.tournament_3 = Tournament(15, self.part_1, self.part_2, self.part_3)  # создаем объект класса Забег

        self.all_results = self.tournament_3.start()  # в словарь all_result записываем результат функции (место:участн)
        last_runner_name = self.all_results[
            max(self.all_results.keys())].name  # записываем имя с максимальным местом
        self.assertTrue(last_runner_name == 'Ник')  # вызываем юнит-метод сравнения
        TournamentTest.all_results[3] = self.all_results  # записываем словарь с ключом 3


if __name__ == "__main__":
    unittest.main()
