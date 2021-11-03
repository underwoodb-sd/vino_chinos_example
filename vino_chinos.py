"""Module for solving the vino chinos problem:

Print the numbers 1 to 100, each on a separate line, to standard out, with the
following qualifications:

- If the number is divisible by 3, print "Vino"
- If the number is divisible by 5, print "Chinos"
- If the number is divisible by 3 and 5, print "Vino Chinos"
- Otherwise, just print the number
"""


def vino_chino_converter(num):
    """Convert number based on vino chino algorithm"""
    if num % 15 == 0:
        return "Vino Chinos"
    if num % 3 == 0:
        return "Vino"
    if num % 5 == 0:
        return "Chinos"
    return str(num)


def vino_chino_mapper(num_list):
    """Map vino chino converter across given list"""
    return list(map(vino_chino_converter, num_list))


def vino_chino_printer(num_list):
    """Prints vino chinos list"""
    vc_list = vino_chino_mapper(num_list)
    if not vc_list:
        print("Nothing to print.")
    for vc in vc_list:
        print(vc)


if __name__ == "__main__":
    vino_chino_printer(list(range(1, 101)))
