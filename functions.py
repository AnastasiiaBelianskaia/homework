def bigger_number(first, second):
    if first > second:
        return first
    return second


def smaller_number(one, two, three):
    if one < two and one < three:
        return one
    if two < one and two < three:
        return two
    return three


def module(figure):
    if figure >= 0:
        return figure
    return figure * (-1)


def sum_of_num(number_one, number_two):
    answer = number_one + number_two
    print('the answer is: ', answer)


def positive_negative(count):
    if count > 0:
        print('Number ', count, 'is positive')
        return count
    if count == 0:
        print('Number ', count, 'is not positive or negative')
        return count
    print('Number ', count, 'is negative')
    return count
