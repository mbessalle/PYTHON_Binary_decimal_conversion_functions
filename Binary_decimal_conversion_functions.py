""" Functions that convert: a binary number to a decimal, a decimal to binary and list of binary numbers to decimals """


""" Turns decimal number to binary number """


def to_binary(number):
    binary_number = str()
    if number != 0:
        while number >= 1:
            if number % 2 == 0:
                binary_number += "0"
                number = number/2
            else:
                binary_number += "1"
                number = (number-1)/2

    else:
        binary_number = "0"
    return str().join(reversed(binary_number))


""" Turns binary number (as a string) to decimal number """


def to_decimal(binary_number):
    index = 0
    binary_list = list(binary_number)
    binary_length = len(binary_list)
    power = binary_length - 1
    decimal = 0
    while power >= 0:
        decimal += (int(binary_list[index]))*(2**power)
        index += 1
        power -= 1
    return decimal


""" Turns list of binary numbers (e.g. ['1001', '01101']) into decimal numbers """


def binary_list_to_decimal(bi_list):
    msg = []
    for i in bi_list:
        decimal_number = to_decimal(i)
        msg.append(decimal_number)
    return msg


