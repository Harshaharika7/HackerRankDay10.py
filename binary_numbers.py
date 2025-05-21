if __name__ == '__main__':
    n = int(input())

    # Convert to binary and remove the '0b' prefix
    binary = bin(n)[2:]

    # Split the binary string at '0' to get groups of consecutive '1's
    ones_groups = binary.split('0')

    # Find the length of the longest group
    max_consecutive_ones = max(len(group) for group in ones_groups)

    print(max_consecutive_ones)
