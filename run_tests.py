import os


def execute_pytest_test(test_name):
    os.system(f"pytest -v -k \"{test_name}\"")


def print_test_options():
    print(" Bienvenido a las pruebas de EDA ".center(80, "="))
    print("1. Todas las estructuras")
    print("2. Listas")
    print("     2.A Lista de arreglos")
    print("     2.B Lista encadenadas")
    print("0. Salir")


def execute_all_tests():
    execute_list_tests()


def execute_list_tests(input_option="2"):
    tests_names = []
    if input_option.lower() == "2.a" or input_option == "2":
        tests_names.append("test_array_list")
    if input_option.lower() == "2.B" or input_option == "2":
        tests_names.append("test_single_linked_list")
    for test_name in tests_names:
        execute_pytest_test(test_name)


if __name__ == "__main__":
    """
    Menu principal de pruebas
    """
    runned = False
    print_test_options()
    input_option = str(input(
        "Ingrese el número de la opción que desea ejecutar: \n"))

    if input_option == "1":
        execute_all_tests()
        runned = True

    if input_option.startswith("2"):
        execute_list_tests(input_option)
        runned = True

    if input_option == "0":
        print("Saliendo de las pruebas")

    elif runned == False:
        print("Opción no válida")

    print(" Gracias por ejecutar las pruebas ".center(80, "="))
