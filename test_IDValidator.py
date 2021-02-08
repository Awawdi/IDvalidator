def validity_check(id_number):
    list_of_IDs = list(map(int, str(id_number)))

    list_of_IDs[1::2] = map(lambda x: x * 2, list_of_IDs[1::2])
    list_of_IDs = map(lambda x: (x % 10 + x // 10), list_of_IDs)
    num1 = sum(list_of_IDs)
    if num1 % 10 != 0:
        return "BAD ID NUMBER"
    else:
        return True

def test_Validator():
    assert validity_check('123456873') == True