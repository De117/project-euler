package problems;

import common.Combinatorics;
import common.PrimeGenerator;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Euler41 {
    /*
    Pandigital prime
    Problem 41

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
    and is also prime.

    What is the largest n-digit pandigital prime that exists?
     */
    public long solution() {
        PrimeGenerator primes = new PrimeGenerator();
        long largestNPandigitalPrime = 0;

        for (int nDigits = 2; nDigits <= 9; nDigits++) {
            List<Integer> digits = Arrays.asList(1,2,3,4,5,6,7,8,9).subList(0, nDigits);

            List<List<Integer>> nPandigitalNumbers = Combinatorics.permutations(digits);

            for (List<Integer> numberAsList : nPandigitalNumbers) {
                long n = numberAsList.stream().reduce(0, (acc, x) -> 10*acc + x);
                if (primes.isPrime(n)) {
                    if (n > largestNPandigitalPrime) {
                        largestNPandigitalPrime = n;
                    }
                }
            }
        }
        return largestNPandigitalPrime;
    }
}
