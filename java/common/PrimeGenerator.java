package common;

import java.util.ArrayList;
import java.util.List;

public class PrimeGenerator {

    // global cache of primes
    private static ArrayList<Long> cache = new ArrayList<>(List.of(2L));

    private long lastPrime = 1;

    private int cacheIndex = 0;

    public long nextPrime() {

        // Fast track: cache lookup
        if (this.cacheIndex < cache.size()) {
            long p = cache.get(this.cacheIndex++);
            this.lastPrime = p;
            return p;
        }

        // Normal computation
        if (lastPrime == 1 || lastPrime == 2) {
            lastPrime = lastPrime + 1;
            cache.add(lastPrime); cacheIndex++;
            return lastPrime;
        }

        long next = lastPrime + 2;
        while (!isPrime(next)) {
            next += 2;
        }
        lastPrime = next;
        cache.add(lastPrime); cacheIndex++;
        return lastPrime;
    }

    public boolean isPrime(long N) {
        long upperBound = (long)Math.ceil(Math.sqrt(N));

        if (N <= 1) {
            return false;
        } else if (N <= 3) {
            return true;
        } else if (N % 2 == 0) {
            return false;
        }

        for (long i = 3; i <= upperBound; i+=2) {
            if (N % i == 0) {
                return false;
            }
        }

        return true;
    }
}
