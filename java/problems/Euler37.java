package problems;

import common.PrimeGenerator;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Euler37 {
    /*
    Truncatable primes
    Problem 37

    The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain
    prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
    right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from
    left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
     */
    public long solution() {
        List<Long> truncatablePrimes = new ArrayList<>();

        PrimeGenerator primes = new PrimeGenerator();
        primes.nextPrime(); // 2
        primes.nextPrime(); // 3
        primes.nextPrime(); // 5
        primes.nextPrime(); // 7
        long p = primes.nextPrime();

        while (truncatablePrimes.size() < 11) {
            List<Long> digits = String.valueOf(p).chars().mapToLong(c -> c - '0').boxed().collect(Collectors.toList());
            boolean isTruncatable = true;
            for (int i = 1; i < digits.size(); i++) {
                // Is it left-to-right truncatable?
                long p1 = digits.subList(i, digits.size()).stream().reduce(0L, (acc, digit) -> 10*acc + digit);
                if (!primes.isPrime(p1)) {
                    isTruncatable = false;
                    break;
                }

                // Is it right-to-left truncatable?
                long p2 = digits.subList(0, digits.size() - i).stream().reduce(0L, (acc, digit) -> 10*acc + digit);
                if (!primes.isPrime(p2)) {
                    isTruncatable = false;
                    break;
                }
            }

            if (isTruncatable) {
                truncatablePrimes.add(p);
            }

            p = primes.nextPrime();
        }
        return truncatablePrimes.stream().reduce(0L, Long::sum);
    }
}
