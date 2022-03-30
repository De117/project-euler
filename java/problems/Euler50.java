package problems;

import common.PrimeGenerator;

import java.util.*;

public class Euler50 {
    /*
    Consecutive prime sum
    Problem 50

    The prime 41, can be written as the sum of six consecutive primes:
        41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime
    below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds
    to a prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the
    most consecutive primes?
     */
    public long solution() {
        // This is few enough primes that we can do an O(n²) loop through them.

        // First, let's get all the primes.
        PrimeGenerator primes = new PrimeGenerator();
        List<Long> primesBelow1M = new ArrayList<>();
        for (long p = primes.nextPrime(); p < 1_000_000; p = primes.nextPrime()) {
            primesBelow1M.add(p);
        }

        // list of (startIndex, runLength) pairs
        List<Pair<Integer, Integer>> matchingSequences = new ArrayList<>();

        for (int i = 0; i < primesBelow1M.size(); i++) {
            long sum = primesBelow1M.get(i);
            for (int j = i + 1; j < primesBelow1M.size(); j++) {
                sum += primesBelow1M.get(j);
                if (sum >= 1_000_000) {
                    break;
                }
                if (primes.isPrime(sum)) {
                    matchingSequences.add(new Pair<>(i, (j - i)));
                }
            }
        }

        matchingSequences.sort(Comparator.comparing(a -> a.second));
        Pair<Integer, Integer> best = matchingSequences.get(matchingSequences.size() - 1);
        int startIndex = best.first;
        int runLength = best.second;

        return primesBelow1M.subList(startIndex, startIndex + runLength + 1).stream().reduce(0L, Math::addExact);
    }
}

class Pair<A, B> {
    public final A first;
    public final B second;
    public Pair(A first, B second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Pair<?, ?> pair = (Pair<?, ?>) o;
        return first.equals(pair.first) && second.equals(pair.second);
    }

    @Override
    public int hashCode() {
        return Objects.hash(first, second);
    }
}
