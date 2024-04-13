# Problem 67 (Maximum Path Sum II)
# ================================
#
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#
#       *3*
#      *7* 4
#     2 *4* 6
#    8 5 *9* 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt
# (right click and 'Save Link/Target As...'),
# a 15K text file containing a triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18.
# It is not possible to try every route to solve this problem,
# as there are 2^99 altogether! If you could check one trillion
# (10^12) routes every second it would take over twenty billion
# years to check them all. There is an efficient algorithm to solve it. ;o)



# Apart from loading the triangle, the solution is an exact copy of problem 18,
# with some parametrization. The "efficient algorithm" is dynamic programming.

triangle = []

if __name__ == "__main__":
    with open("../p067_triangle.txt") as f:
        for line in f:
            triangle.append([int(n) for n in line.split()])

    N = len(triangle)

    # Instead of going top to bottom, we start at the bottom and
    # choose the best path upwards.

    # At the start, the best routes are bottom layer elements themselves.
    best = triangle[N-1]

    # Then, for a node in an unvisited layer, the best route to it leads
    # through the best "child" node.
    for depth in reversed(range(N-1)):
        new_best = []
        for i, e in enumerate(triangle[depth]):
            new_best.append(e + max(best[i], best[i+1]))
        best = new_best

    print(best[0])
