def fib(n):
    """
    Calculate the nth Fibonacci number.

    Parameters:
    n (int): The index of the Fibonacci number to calculate.

    Returns:
    int: The nth Fibonacci number.

    """
    # TODO: Implement the fib function
    pass

def main():
    import sys
    if len(sys.argv) < 2:
        print("Please provide the number of the Fibonacci number you want to calculate.")
        sys.exit(1)
    n = int(sys.argv[1])
    print(fib(n))

if __name__ == '__main__':
    main()