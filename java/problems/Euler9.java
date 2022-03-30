package problems;

public class Euler9 {

    /*
    Special Pythagorean triplet
    Problem 9

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a² + b² = c²

    For example, 3² + 4² = 9 + 16 = 25 = 5².

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
     */
    public long solution() {
        long product = 0;
        outerloop:
        for (long a = 2; a < 1000; a++) {
            for (long b = a + 1; b < 1000; b++) {
                long c = 1000 - a - b;
                if (a*a + b*b == c*c) {
                    // Pythagorean triplet
                    product = a*b*c;
                    break outerloop;
                }
            }
        }
        return product;
    }
}
