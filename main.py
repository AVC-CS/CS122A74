
def deleteElements(numbers, value):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while True:
        try:
            numbers.remove(value)
        except ValueError:
            break   

def main():
    numbers = [5, 20, 30, 30, 35]
    print(f'\n***************** Test 1: Delete 30 *****************')
    print(f'Original list value: {numbers}')
    deleteElements(numbers, 30)
    print(f'After deleting 30 {numbers}, should not have any 30s now')

    numbers = [1, 1, 1, 1, 1]
    print(f'\n***************** Test 2: Delete all 1\'s *****************')
    print(f'Original list value: {numbers}')
    deleteElements(numbers, 1)
    print(f'After deleting 1 {numbers}, should be empty list now')


if __name__ == '__main__':
    main()
