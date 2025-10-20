import main
import pytest

@pytest.mark.basic
def test_main_1():
    numbers = [5, 20, 30, 30, 35]
    print('***************** Test 1: Delete 30 *****************')
    print(f'Original list value: {numbers}')
    main.deleteOne(numbers, 30)
    print(f'After deleting 30 {numbers}, should not have any 30s now')
    assert numbers == [5, 20, 35], f'Expected [5, 20, 35] but got {numbers}'

@pytest.mark.edge
def test_main_2():
    numbers = [1, 1, 1, 1, 1]
    print('***************** Test 2: Delete all 1\'s *****************')
    print(f'Original list value: {numbers}')
    main.deleteOne(numbers, 1)
    print(f'After deleting 1 {numbers}, should be empty list now')
    assert numbers == [], f'Expected [] but got {numbers}'

@pytest.mark.bonus
def test_main_3():
    numbers = [1, 2, 3, 4, 5]
    print('***************** Test 3: Delete non-existing value 6 *****************')
    print(f'Original list value: {numbers}')
    main.deleteOne(numbers, 6)
    print(f'After deleting 6 {numbers}, should be unchanged')
    assert numbers == [1, 2, 3, 4, 5], f'Expected [1, 2, 3, 4, 5] but got {numbers}'
