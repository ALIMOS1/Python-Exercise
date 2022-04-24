# Return true if any number is even inside a list
# The return breaks out of the loop 


def check_even(number_list):
    even_numbers = []
    for number in number_list:
        if number%2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

