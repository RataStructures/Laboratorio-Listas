from DataStructures.List import list_node as ln

# Funciones auxiliares
# Estas funciones NO son parte de la API y NO deben ser utilizadas directamente.
# Son funciones auxiliares internas para la implementación del módulo.


def update_first(my_list, node):
    my_list["first"] = node
    return my_list


def update_last(my_list, node):
    my_list["last"] = node
    return my_list


def get_first(my_list):
    first = my_list["first"]
    return first


def get_last(my_list):
    last = my_list["last"]
    return last


def increment_size(my_list):
    my_list["size"] += 1
    return my_list


def decrease_size(my_list):
    my_list["size"] -= 1
    return my_list


def update_size(my_list, size):
    my_list["size"] = size
    return my_list


def update_list(my_list, new_list):
    my_list = update_first(my_list, get_first(new_list))
    my_list = update_last(my_list, get_last(new_list))
    my_list = update_size(my_list, size(new_list))
    return my_list


def iterator_node(my_list, start, end, step):
    first_node = get_first(my_list)
    current_node = ln.get_node(first_node, start)
    index = start
    while current_node is not None and index < end:
        if index >= start and (index - start) % step == 0:
            yield current_node
        index += step
        current_node = ln.get_node(current_node, step)


# Función extra (no documentada en la API) que permite iterar sobre los elementos de la lista


def iterator(my_list, start, end, step):
    first_node = get_first(my_list)
    current_node = ln.get_node(first_node, start)
    index = start
    while current_node is not None and index < end:
        if index >= start and (index - start) % step == 0:
            current_value = ln.get_element(current_node)
            yield current_value
        index += step
        current_node = ln.get_node(current_node, step)


# Funciones principales de la API


def default_function(element_1, element_2):
    if element_1 == element_2:
        response = 0
    elif element_1 > element_2:
        response = 1
    else:
        response = -1
    return response


def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted


def new_list():
    first, last, size = None, None, 0
    my_list = {"first": first, "last": last, "size": size}
    return my_list


def is_empty(my_list):
    return my_list["size"] == 0


def size(my_list):
    return my_list["size"]


def add_first(my_list, element):
    node = ln.new_single_node(element)
    if is_empty(my_list):
        my_list = update_first(my_list, node)
        my_list = update_last(my_list, node)
    else:
        first_node = get_first(my_list)
        node = ln.update_next(node, first_node)
        my_list = update_first(my_list, node)
    my_list = increment_size(my_list)
    return my_list


def add_last(my_list, element):
    node = ln.new_single_node(element)
    if is_empty(my_list):
        my_list = update_first(my_list, node)
        my_list = update_last(my_list, node)
    else:
        last_node = get_last(my_list)
        last_node = ln.update_next(last_node, node)
        my_list = update_last(my_list, node)
    my_list = increment_size(my_list)
    return my_list


def first_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        first_node = get_first(my_list)
        first = ln.get_element(first_node)
    return first


def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        last_node = get_last(my_list)
        last = ln.get_element(last_node)
    return last


def get_element(my_list, pos):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        first_node = get_first(my_list)
        node = ln.get_node(first_node, pos)
        element = ln.get_element(node)
    return element


def delete_element(my_list, pos):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        if pos == 0:
            _ = remove_first(my_list)
        elif pos == n - 1:
            _ = remove_last(my_list)
        else:
            first_node = get_first(my_list)
            prev_node = ln.get_node(first_node, pos - 1)
            next_node = ln.get_node(first_node, pos + 1)
            prev_node = ln.update_next(prev_node, next_node)
            my_list = update_first(my_list, first_node)
            my_list = decrease_size(my_list)
    return my_list


def remove_first(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        n = size(my_list)
        if n == 1:
            removed_element = first_element(my_list)
            my_list = update_first(my_list, None)
            my_list = update_last(my_list, None)
            my_list = decrease_size(my_list)
        else:
            first_node = get_first(my_list)
            removed_element = ln.get_element(first_node)
            next_node = ln.get_next(first_node)
            my_list = update_first(my_list, next_node)
            my_list = decrease_size(my_list)
    return removed_element


def remove_last(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        n = size(my_list)
        if n == 1:
            removed_element = first_element(my_list)
            my_list = update_first(my_list, None)
            my_list = update_last(my_list, None)
            my_list = decrease_size(my_list)
        else:
            last_node = get_last(my_list)
            removed_element = ln.get_element(last_node)
            first_node = get_first(my_list)
            prev_node = ln.get_node(first_node, n - 2)
            prev_node = ln.update_next(prev_node, None)
            my_list = update_last(my_list, prev_node)
            my_list = decrease_size(my_list)
    return removed_element


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
            first = get_first(my_list)
            prev_node = ln.get_node(first, pos - 1)
            next_node = ln.get_node(first, pos)
            node = ln.new_single_node(element)
            prev_node = ln.update_next(prev_node, node)
            node = ln.update_next(node, next_node)
            my_list = update_first(my_list, first)
            my_list = increment_size(my_list)
    return my_list


def is_present(my_list, element, cmp_function):
    result, index, n = -1, 0, size(my_list)
    for current in iterator(my_list, 0, n, 1):
        are_equal = cmp_function(element, current) == 0
        if are_equal:
            result = index
            break
        index += 1
    return result


def change_info(my_list, pos, new_info):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        first_node = get_first(my_list)
        node = ln.get_node(first_node, pos)
        node = ln.update_info(node, new_info)
        my_list = update_first(my_list, first_node)
    return my_list


def exchange(my_list, pos_1, pos_2):
    n = size(my_list)
    if pos_1 < 0 or pos_1 >= n or pos_2 < 0 or pos_2 >= n:
        raise Exception("IndexError: list index out of range")
    else:
        first_node = get_first(my_list)
        node_1 = ln.get_node(first_node, pos_1)
        node_2 = ln.get_node(first_node, pos_2)
        info_1 = ln.get_element(node_1)
        info_2 = ln.get_element(node_2)
        node_1 = ln.update_info(node_1, info_2)
        node_2 = ln.update_info(node_2, info_1)
        my_list = update_first(my_list, first_node)
    return my_list


def sub_list(my_list, pos, num_elements):
    n = size(my_list)
    if pos < 0 or pos >= size(my_list) or num_elements < 0 or pos + num_elements > n:
        raise Exception("IndexError: list index out of range")
    else:
        sublist, index = new_list(), 0
        for current in iterator(my_list, 0, n, 1):
            if index >= pos and index < pos + num_elements:
                sublist = add_last(sublist, current)
            if index == pos + num_elements:
                break
            index += 1
    return sublist