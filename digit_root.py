class digit_root():
    def __init__(self):
        self.number = None

    def prompt_user(self):
        try:
            self.number = int(input('Type any natural number from 0 to 10^7:  '))
            if self.number < 1 or self.number > 10**7:
                raise ValueError('The number is out of range')
        except ValueError as e:
            print(e)

    def calc_root(self):
        str_number=str(self.number)
        while len(str_number) > 1:
            total_sum = 0
            for digit in str_number:
                total_sum += int(digit)
            str_number = str(total_sum)
        return int(str_number)


my_digit = digit_root()
my_digit.prompt_user()
print(my_digit.calc_root())
