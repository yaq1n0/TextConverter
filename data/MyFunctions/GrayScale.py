# function to create GrayScale string


def GrayScale(num):
    if type(num) == int:
        if 0 <= num <= 255:
            h_num_str = str(hex(num))

            if len(h_num_str) == 3:
                num3 = "0" + h_num_str[-1]

            elif len(h_num_str) == 4:
                num3 = h_num_str[-2] + h_num_str[-1]

            else:
                print('error: too many or few digits in input')
                return '#FF2020'

            return '#' + str(num3) + str(num3) + str(num3)
        else:
            print('error: input out of range')
            return '#FF2020'
    else:
        print('error: wrong data type in input')
        return '#FF2020'


if __name__ == '__main__':
    for n in range(-20, 261, 40):
        print('GrayScale of:', n, 'is', GrayScale(n))
        print('------------------------------')

    n = 'I\'m a string look at me'
    print('GrayScale of: ' + '"' + n + '" is', GrayScale(n))
    print('------------------------------')
