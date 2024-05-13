import sys

def solve(n):
    """
    Solves the Tower of Hanoi puzzle for a given number of disks.

    Parameters:
    n (int): The number of disks in the puzzle.

    Returns:
    None
    """
    def move(n, source, target, auxiliary):
        # TODO: Implement the move function
        print(f"Move disk {n} from {source} to {target}") # Leave this line as is

    move(n, 'A', 'C', 'B')

def main():
    if len(sys.argv) < 2:
        print("Please provide the number of rings as a command line argument.")
        return

    n = int(sys.argv[1])
    solve(n)

if __name__ == '__main__':
    main()