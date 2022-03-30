package problems;

import java.math.BigInteger;

public class Euler15 {

    /*
    Lattice paths
    Problem 15

    Starting in the top left corner of a 2×2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right corner.

    ooooooo    oooo--+    oooo--+
    |  |  o    |  o  |    |  o  |
    +--+--o    +--oooo    +--o--+
    |  |  o    |  |  o    |  o  |
    +--+--V    +--+--V    +--ooo>

    o--+--+    o--+--+    o--+--+
    o  |  |    o  |  |    o  |  |
    ooooooo    oooo--+    o--+--+
    |  |  o    |  o  |    o  |  |
    +--+--V    +--ooo>    oooooo>

    How many such routes are there through a 20×20 grid?
     */
    public long solution() {
        int N = 20;
        // This problem is equivalent to:
        //
        // "In how many ways can we get from (0,0) to (20,20)
        // by adding either (1,0) or (0,1)?"
        //
        // That is, how many different sequences are there?
        // In how many ways can we order twenty "(1,0)"s and twenty "(0,1)"s?
        //
        // Or: given an urn with 20 white balls and 20 red balls, in how many
        //     ways can we take them out one by one?

        // (2*N)! / (N! * N!)
        BigInteger numerator = fact(2*N);
        BigInteger denominator = fact(N).multiply(fact(N));
        return numerator.divide(denominator).longValueExact();
    }

    private BigInteger fact(long N) {
        BigInteger product = BigInteger.ONE;
        for (int i = 2; i <= N; i++) {
            product = product.multiply(BigInteger.valueOf(i));
        }
        return product;
    }
}
