package problems;

import java.math.BigInteger;
import java.util.HashSet;
import java.util.Set;

public class Euler29 {
    /*
    Distinct powers
    Problem 29

    Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

        2²=4, 2³=8, 2⁴=16, 2⁵=32
        3²=9, 3³=27, 3⁴=81, 3⁵=243
        4²=16, 4³=64, 4⁴=256, 4⁵=1024
        5²=25, 5³=125, 5⁴=625, 5⁵=3125

    If they are then placed in numerical order, with any repeats removed,
    we get the following sequence of 15 distinct terms:

        4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

    How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
     */
    public long solution() {
        Set<BigInteger> terms = new HashSet<>();
        for (int a = 2; a <= 100; a++) {
            for (int b = 2; b <= 100; b++) {
                BigInteger n = BigInteger.valueOf(a).pow(b);
                terms.add(n);
            }
        }
        return terms.size();
    }
}
