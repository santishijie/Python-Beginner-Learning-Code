import pytest

from employee import Employee


@pytest.fixture
def example_employee():
    example_employee = Employee("tom", "stack", 25000)
    return example_employee


def test_give_default_raise(example_employee):
    # Employee_01 = Employee("tom", "stack", 25000)
    example_employee.give_raise()
    assert example_employee.salary == 30000


def test_give_custom_raise(example_employee):
    # Employee_01 = Employee("tom", "stack", 25000)
    example_employee.give_raise(10000)
    assert example_employee.salary == 35000
