import pytest
from app.calculator import Calculator


class TestCalcPositive:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_success_multiply(self):
        assert self.calc.multiply(self, 4, 0) == 0

    def test_success_division(self):
        assert self.calc.division(self, 16, 4) <= 4

    def test_success_subtraction(self):
        assert self.calc.subtraction(self, 18, 1) > 5

    def test_success_adding(self):
        assert self.calc.adding(self, 9, 5) != 8

    def test_success_percent(self):
        assert self.calc.percent(self, 0.10, 50) == 0.2

    def teardown(self):
        print('Тест завершен!')