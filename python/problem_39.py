# Problem 39 (Integer right triangles)
# ====================================
#
# If p is the perimeter of a right angle triangle with integral length
# sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?
if __name__ == "__main__":

    solutions = {}

    for p in range(1000+1):
        solutions[p] = set()
        for a in range(1, (p - 2)+1):
            for b in range(1, (p - 2 - a)+1):
                c = p - a - b
                if a*a + b*b == c*c:
                    triple = tuple(sorted((a,b,c)))
                    solutions[p].add(triple)

    _, p_argmax = max((len(v), p) for p,v in solutions.items())
    print(p_argmax)
