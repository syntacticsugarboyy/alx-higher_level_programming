#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    sol = 0
    for idx in range(list_length):
        try:
            sol = my_list_1[idx] / my_list_2[idx]
        except (TypeError):
            sol = 0
            print('wrong type')
        except ZeroDivisionError:
            sol = 0
            print('division by 0')
        except IndexError:
            sol = 0
            print('out of range')
        finally:
            pass
        new_list.append(sol)
    return new_list
