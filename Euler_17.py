"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.
If all the numbers from 1 to 1000 one thousand inclusive were written out in words,
how many letters would be used?
Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""


def under_thousand_to_string():
    digits_as_strings = {
                        0: '',
                        1: 'one',
                        2: 'two',
                        3: 'three',
                        4: 'four',
                        5: 'five',
                        6: 'six',
                        7: 'seven',
                        8: 'eight',
                        9: 'nine',
                        10: 'ten',
                        11: 'eleven',
                        12: 'twelve',
                        13: 'thirteen',
                        14: 'fourteen',
                        15: 'fifteen',
                        16: 'sixteen',
                        17: 'seventeen',
                        18: 'eighteen',
                        19: 'nineteen',
                        20: 'twenty',
                        30: 'thirty',
                        40: 'forty',
                        50: 'fifty',
                        60: 'sixty',
                        70: 'seventy',
                        80: 'eighty',
                        90: 'ninety',
                        1000: 'onethousand'}
    
    s = 0

    def parse_2_digits(number_str: str):
        if int(number_str) in digits_as_strings:
            return digits_as_strings[int(number_str)]
        str_2_digits = ''
        two_digits = int(number_str[:1] + '0')
        str_2_digits += digits_as_strings[two_digits]
        last_dig = digits_as_strings[int(number_str[-1])]
        str_2_digits += last_dig
        return str_2_digits
    
    for n in range(1, 1001):
        num_str = ''
        n_str = str(n)
        if n in digits_as_strings:  # Check i fnum in dict
            num_str = digits_as_strings[n]  # We have answer
        else:
            if len(n_str) == 2:  # Two digit number (all 1 digit in dict)
                num_str += parse_2_digits(n_str)
            else:  # == 3 digit number (thousand in dict)
                num_str += digits_as_strings[int(n_str[:1])]
                num_str += 'hundred'
                digits23 = n_str[1:]
                two_dig_str = parse_2_digits(digits23)
                if two_dig_str:
                    num_str += 'and'
                    num_str += two_dig_str
        print(num_str)
        s += len(num_str)
    print(s)


under_thousand_to_string()
