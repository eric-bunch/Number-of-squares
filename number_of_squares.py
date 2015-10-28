def answer(n):
    """
    Lagrange's four-square theorem tells us that 
    every positive integer can be written as the 
    sum of the squares of four integers. So our output 
    will always be between one and four. 
    
    Legendre's three-square theorem gives a condition 
    that completely characterizes whether or not a 
    positive integer is the sum of the squares of three 
    integers. 
    """
    
    squares_leq_n = [x**2 for x in range(1, n) if x**2 <= n]
    
    # Here we are using the fact that we know the upper bound for n.
    for a in range(0, 8):
        for b in range(0, 1250):
            # This is the condition from Legendre's three-square 
            # theorem for a positive integer to NOT be the sum of 
            # the squares of three integers
            if (4**a)*(8*b + 7) == n:
                # If n is not the sum of the squares of three 
                # integers, then it must the sum of four (by Lagrange)
                return 4
    # Check two cases by brute force
    else:
        # Check to see if n is a perfect square
        for a in squares_leq_n:
            if a == n:
                return 1
        else:
            # Check to see if n is the sum of two squares
            for (a, b) in [(x, y) for x in squares_leq_n for y in squares_leq_n]:
                if a + b == n:
                    return 2
            else:
                # If n is not a square or the sum of two squares, since we have 
                # already determined that it is the sum of three or less 
                # squares, n must be the sum of three squares.
                return 3
 
