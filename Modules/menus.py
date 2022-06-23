from .data import data_compiler as compiler


def printer():
    """ Function used to print out the main menu for user selections. """

    data = compiler()
    j = 0

    menu_list = [i for i in data[0]]

    print(f"{'#' * 50}\n{'#' * 50}\n"
            + f"\n{' ' * 20}Main Menu\n")

    for i in menu_list:
        output = f"{j}  {str(i).upper()}"
        print(output)
        j += 1

    print(f"\n{'#' * 50}\n{'#' * 50}")
