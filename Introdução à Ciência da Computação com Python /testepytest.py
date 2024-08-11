def func(x):
    return x + 1
def test_answer():
    try:
     assert func(3) == 4
     return "Test passed"

    except AssertionError:
        return "Test failed"
print(test_answer())