package problems;

import common.PrimeGenerator;

import java.util.ArrayList;
import java.util.List;

public class Euler46 {
    /*
    Goldbach's other conjecture
    Problem 46

    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.

        9 = 7 + 2×1²
        15 = 7 + 2×2²
        21 = 3 + 2×3²
        25 = 7 + 2×3²
        27 = 19 + 2×2²
        33 = 31 + 2×1²

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of
    a prime and twice a square?
     */
    public long solution() {
        // From the problem description, most of them *can* be written like so.
        // So, instead of testing each one, it may be more reasonable to sieve
        // out those which can, and take a look at what's left.
        int upperBound = 100;
        while (true) {
            PrimeGenerator primes = new PrimeGenerator();
            boolean[] sieve = new boolean[upperBound];

            for (long p = primes.nextPrime(); p < upperBound; p = primes.nextPrime()) {
                for (int i = 0; ; i++) {
                    int x = (int) p + 2 * i * i;
                    if (x >= upperBound) {
                        break;
                    }
                    sieve[x] = true;
                }
            }

            // Find the first one which _cannot_ be written like so.
            for (int i = 9; i < upperBound; i += 2) {
                if (!sieve[i]) {
                    if (!primes.isPrime(i)) {
                        return i;
                    }
                }
            }

            // If we're here, we haven't found it yet.
            upperBound *= 2;
        }
    }
}
