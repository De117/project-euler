package problems;

import common.PrimeDecomposition;

import java.util.ArrayList;

public class Euler47 {
    /*
    Distinct primes factors
    Problem 47

    The first two consecutive numbers to have two distinct prime factors are:

        14 = 2 × 7
        15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors are:

        644 = 2² × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime factors
    each. What is the first of these numbers?
     */
    public long solution() {
        for (long i = 1; ; i++) {
            if ((new PrimeDecomposition(i)).coefficients.size() == 4
                    && (new PrimeDecomposition(i+1)).coefficients.size() == 4
                    && (new PrimeDecomposition(i+2)).coefficients.size() == 4
                    && (new PrimeDecomposition(i+3)).coefficients.size() == 4)
            {
                return i;
            }
        }
    }
}
