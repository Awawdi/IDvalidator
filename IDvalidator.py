MAX_NUMBER = 999999999

class IDIterator:
    def __init__(self, id):
        self._list_of_ids = []
        self._starting_point = id
        self._pointer = -1
        # self._id = '{:09d}'.format(id)
        self._id = int(str(id).zfill(9))
        # for i in range(999999999):
        #    self._list_of_ids.append('{:09d}'.format(i))

    def __iter__(self):
        return self

    def __next__(self):
        print("next correct ID number:")
        while self._id < MAX_NUMBER:
            self._id += 1
            if validity_check(self._id):
                return self.get_arg()

    def get_arg(self):
        return self._id


class Not9DigitNumber(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "ID needs to be 9 digits exactly: %s" % self._arg

    def get_arg(self):
        return self._arg


class NotADigitInput(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "ID needs to be digits only: %s" % self._arg

    def get_arg(self):
        return self._arg


class WrongIDNumber(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "wrong ID number: %s" % self._arg

    def get_arg(self):
        return self._arg


def validity_check(id_number):
    list_of_IDs = list(map(int, str(id_number)))

    list_of_IDs[1::2] = map(lambda x: x * 2, list_of_IDs[1::2])
    list_of_IDs = map(lambda x: (x % 10 + x // 10), list_of_IDs)
    num1 = sum(list_of_IDs)
    if num1 % 10 != 0:
        return False
    else:
        return True


def main():
    '''
    id_number = input("Please enter ID Number")

    try:
        if not id_number.isdigit():
            raise NotADigitInput(id_number)
        if not len(id_number) == 9:
            raise Not9DigitNumber(id_number)
        if not validity_check(id_number):
            raise WrongIDNumber(id_number)
        else:
            print("Valid ID!")

    except NotADigitInput as eNotADigitInput:
        print(eNotADigitInput)
    except Not9DigitNumber as eNot9DigitNumber:
        print(eNot9DigitNumber)
    except WrongIDNumber as eWrongIDnumber:
        print(eWrongIDnumber)

    '''
    IDiterable = IDIterator("123456780")
    IDiterator = iter(IDiterable)

    for itr in range(10):
        print(next(IDiterable))



main()
