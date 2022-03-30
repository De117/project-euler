package problems;

import common.PrimeGenerator;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Euler35 {
    /*
    Circular primes
    Problem 35

    The number, 197, is called a circular prime because all rotations
    of the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100:
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?
     */
    public long solution() {
        List<Long> circularPrimes = new ArrayList<>();
        PrimeGenerator primes = new PrimeGenerator();

        long p = primes.nextPrime();
        while (p < 1_000_000) {
            List<Long> digits = String.valueOf(p).chars().mapToLong(c -> c - '0').boxed().collect(Collectors.toList());

            boolean isCircular = true;
            for (int i = 1; i < digits.size(); i++) {
                Collections.rotate(digits, 1);  // rotate right
                long number = digits.stream().reduce(0L, (acc, digit) -> 10*acc + digit);

                if (!primes.isPrime(number)) {
                    isCircular = false;
                    break;
                }
            }

            if (isCircular) {
                circularPrimes.add(p);
            }

            p = primes.nextPrime();
        }

        return circularPrimes.size();
    }
}
