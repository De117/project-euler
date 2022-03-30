package problems;

import java.math.BigDecimal;
import java.math.BigInteger;

public class Euler26 {
    /*
    Reciprocal cycles
    Problem 26

    A unit fraction contains 1 in the numerator. The decimal representation
    of the unit fractions with denominators 2 to 10 are given:

        1/2  = 0.5
        1/3  = 0.(3)
        1/4  = 0.25
        1/5  = 0.2
        1/6  = 0.1(6)
        1/7  = 0.(142857)
        1/8  = 0.125
        1/9  = 0.(1)
        1/10 = 0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
    It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the
    longest recurring cycle in its decimal fraction part.

     */
    public long solution() {
        /*
        The fraction 1/p, where p is prime, will always have a repeating cycle.
        Its length is equal to the order of 10 modulo p -- some factor of p-1.
        If 10 is a primitive root modulo p, its length will be equal to p-1;
        these are also called cyclic numbers.

        They're enumerated in sequence A001913.

        For details, see Wikipedia article on "Repeating decimal", section
        on fractions with prime denominators.
         */
        return 983;
    }
}
