package common;

import java.util.*;
import java.util.function.BinaryOperator;

public class PrimeDecomposition {

    public Map<Long, Long> coefficients;

    public PrimeDecomposition(long N) {
        if (N < 1) {
            String message = String.format("Cannot decompose non-natural number: %d", N);
            throw new IllegalArgumentException(message);
        }
        this.coefficients = new TreeMap<>();

        // Special case
        if (isPrime(N)) {
            coefficients.put(N, 1L);
            return;
        }

        // General case
        long upperBound = (long)Math.ceil(Math.sqrt(N));
        PrimeGenerator primes = new PrimeGenerator();

        long prime = primes.nextPrime();
        while (N != 1) {
            if (N % prime == 0) {
                long coef = getArity(N, prime);
                coefficients.put(prime, coef);
                N /= (long)Math.pow(prime, coef);
            }
            prime = primes.nextPrime();
        }
    }

    public PrimeDecomposition(Map<Long, Long> coefficients) {
        this.coefficients = coefficients;
    }

    private long getArity(long N, long prime) {
        long arity = 0;
        while( N % prime == 0) {
            arity++;
            N /= prime;
        }
        return arity;
    }

    private boolean isPrime(long N) {
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


    private PrimeDecomposition elementwise(PrimeDecomposition other, BinaryOperator<Long> f) {
        Map<Long, Long> map = new TreeMap<>();

        // get primes in both decompositions
        Set<Long> primes = new TreeSet<>(this.coefficients.keySet());
        primes.addAll(other.coefficients.keySet());

        // take element-wise operation
        for (long prime : primes) {
            long arity1 = this.coefficients.getOrDefault(prime, 0L);
            long arity2 = other.coefficients.getOrDefault(prime, 0L);
            long result = f.apply(arity1, arity2);
            map.put(prime, result);
        }

        return new PrimeDecomposition(map);
    }

    public PrimeDecomposition intersect(PrimeDecomposition other) {
        return this.elementwise(other, Math::min);
    }

    public PrimeDecomposition union(PrimeDecomposition other) {
        return this.elementwise(other, Math::max);
    }

    public List<Long> getProperDivisors() {
        // We send in a copy, because it will get mutated
        Map<Long, Long> copy = new HashMap<Long, Long>(this.coefficients);
        List<Long> res = _getProperDivisors(copy);
        // Take out the largest divisor, because it's the number itself.
        // (Not a *proper* divisor.)
        res.sort(Long::compareTo);
        return res.subList(0, res.size() - 1);
    }

    private List<Long> _getProperDivisors(Map<Long, Long> coefficients) {
        List<Long> divisors = new ArrayList<>();

        // Base case for recursion -- just 1
        if (coefficients.size() == 0) {
            divisors.add(1L);
            return divisors;
        }

        // Pop a prime from the list of coefficients
        long prime = coefficients.keySet().iterator().next();
        long exponent = coefficients.get(prime);
        coefficients.remove(prime);

        // Send the remaining prime coefficients down the recursion
        List<Long> divisorsSoFar =_getProperDivisors(coefficients);

        // When coming back up the recursion, we multiply all the existing
        // proper divisors with each power of this level's prime number.
        for (long i = 0; i <= exponent; i++) {
            for (long divisor : divisorsSoFar) {
                long factor = (long)Math.pow(prime, i);
                divisors.add(factor * divisor);
            }
        }

        return divisors;
    }

    public long toNumber() {
        long N = 1;

        for (long prime : this.coefficients.keySet()) {
            long coef = this.coefficients.get(prime);
            N *= (long)Math.pow(prime, coef);
        }

        return N;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof PrimeDecomposition) {
            PrimeDecomposition o = (PrimeDecomposition) obj;
            return this.coefficients.equals(o.coefficients);
        }
        return false;
    }
}
