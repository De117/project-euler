package problems;

import common.Combinatorics;
import common.PrimeGenerator;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Euler49 {
    /*
    Prime permutations
    Problem 49

    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms
    are prime, and, (ii) each of the 4-digit numbers are permutations of one
    another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
    exhibiting this property, but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?
     */
    public long solution() {
        PrimeGenerator primes = new PrimeGenerator();
        Set<Long> fourDigitPrimes = new TreeSet<>();
        for (long i = primes.nextPrime(); i < 10000; i = primes.nextPrime()) {
            if (i >= 1000) {
                fourDigitPrimes.add(i);
            }
        }

        for (long p1 : fourDigitPrimes) {
            if (p1 == 1487) { continue; } // we ignore this one

            List<Long> permutations = permutationsOf(p1);
            for (long p2 : permutations) {
                if (p1 != p2 && fourDigitPrimes.contains(p2)) {
                    long p3 = p2 + (p2 - p1);
                    if (permutations.contains(p3) && fourDigitPrimes.contains(p3)) {
                        return p1 * 100000000 + p2 * 10000 + p3;
                    }
                }
            }
        }
        return 0;
    }

    /**
     * Returns permutations of n.
     * @param n
     * @return
     */
    private List<Long> permutationsOf(long n) {
        List<Long> ret = new ArrayList<>();

        List<Long> digits = new ArrayList<>();
        for (char c : String.valueOf(n).toCharArray()) {
            digits.add((long)c - '0');
        }

        for (List<Long> perm : Combinatorics.permutations(digits)) {
            long number = perm.stream().reduce(0L, (acc, digit) -> 10 * acc + digit);
            ret.add(number);
        }
        return ret;
    }
}
