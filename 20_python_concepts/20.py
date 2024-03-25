import pytest

@pytest.fixture
def nums():
    return [1, 2, 3, 4, 5]

def test_list_operation(nums):
    try:
        r = len(nums)
        print("Length of the list:", r)
    except AttributeError:
        print("Error: The list does not have a 'length' attribute.")

if __name__ == "__main__":
    pytest.main([__file__])