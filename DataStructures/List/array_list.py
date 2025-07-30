# Funciones auxiliares
# Estas funciones NO son parte de la API y NO deben ser utilizadas directamente.
# Son funciones auxiliares internas para la implementación del módulo.


def update_list(my_list, elements):
    size = len(elements)
    my_list["elements"] = elements
    my_list["size"] = size
    return my_list


def get_elements(my_list):
    elements = my_list["elements"]
    return elements


# Función extra (no documentada en la API) que permite iterar sobre los elementos de la lista


def iterator(my_list, start, end, step):
    for index in range(start, end, step):
        yield get_element(my_list, index)


# Funciones principales de la API


def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted


def default_function(element_1, element_2):
    if element_1 == element_2:
        response = 0
    elif element_1 > element_2:
        response = 1
    else:
        response = -1
    return response


def new_list():
    elements = []
    size = 0
    my_list = {"elements": elements, "size": size}
    return my_list


def add_first(my_list, element):
    elements = get_elements(my_list)
    elements.insert(0, element)
    my_list = update_list(my_list, elements)
    return my_list


def add_last(my_list, element):
    elements = get_elements(my_list)
    elements.append(element)
    my_list = update_list(my_list, elements)
    return my_list


def is_empty(my_list):
    is_empty = size(my_list) == 0
    return is_empty


def size(my_list):
    size = my_list["size"]
    return size


def first_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        first = elements[0]
    return first


def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        last = elements[-1]
    return last


def get_element(my_list, pos):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        element = elements[pos]
    return element


def remove_first(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        first = elements.pop(0)
        my_list = update_list(my_list, elements)
    return first


def remove_last(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        last = elements.pop()
        my_list = update_list(my_list, elements)
    return last


def insert_element(my_list, element, pos):
    n = size(my_list)
    if pos < 0 or pos > n:
        raise Exception("IndexError: list index out of range")
    else:
        if pos == 0:
            my_list = add_first(my_list, element)
        elif pos == n:
            my_list = add_last(my_list, element)
        else:
            elements = get_elements(my_list)
            elements.insert(pos, element)
            my_list = update_list(my_list, elements)
    return my_list


def is_present(my_list, element, cmp_function):
    result, n = -1, size(my_list)
    for index in range(n):
        current = get_element(my_list, index)
        are_equal = cmp_function(element, current) == 0
        if are_equal:
            result = index
            break
    return result


def delete_element(my_list, pos):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        del elements[pos]
        my_list = update_list(my_list, elements)
    return my_list


def change_info(my_list, pos, new_info):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        elements[pos] = new_info
        my_list = update_list(my_list, elements)
    return my_list


def exchange(my_list, pos_1, pos_2):
    n = size(my_list)
    if pos_1 < 0 or pos_1 >= n or pos_2 < 0 or pos_2 >= n:
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        elements[pos_1], elements[pos_2] = elements[pos_2], elements[pos_1]
        my_list = update_list(my_list, elements)
    return my_list


def sub_list(my_list, pos_i, num_elements):
    n = size(my_list)
    if pos_i < 0 or pos_i >= n or num_elements < 0 or pos_i + num_elements > n:
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        sub_elements = elements[pos_i : pos_i + num_elements]
        my_sub_list = new_list()
        my_sub_list = update_list(my_sub_list, sub_elements)
    return my_sub_list
