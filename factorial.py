def factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number for which factorial needs to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    pass

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please provide the number for which you want to calculate the factorial.")
        sys.exit(1)
    n = int(sys.argv[1])
    print(factorial(n))