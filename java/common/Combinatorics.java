package common;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Combinatorics {

    public static long factorial(long l) {
        long acc = 1;
        if (l < 1)
            return acc;
        for (long i = 1; i <= l; i++) {
            acc *= i;
        }
        return acc;
    }

    public static BigInteger factorial(BigInteger l) {
        BigInteger acc = BigInteger.ONE;
        if (l.compareTo(BigInteger.ONE) < 0) {
            return acc;
        }
        for (BigInteger i = BigInteger.ONE; i.compareTo(l) <= 0; i = i.add(BigInteger.ONE)) {
            acc = acc.multiply(i);
        }
        return acc;
    }

    public static <T extends Comparable<? super T>> List<List<T>>permutations(List<T> input) {
        List<List<T>> ret = new ArrayList<>();

        // Base case
        if (input.size() == 1) {
            ret.add(new ArrayList<T>(input));
            return ret;
        }

        // Recursive case:
        T head = input.get(0);
        List<T> tail = input.subList(1, input.size());

        for (List<T> permutation : permutations(tail)) {
            permutation.add(0, head);
            // Add all rotations
            for (int i = 0; i < permutation.size(); i++) {
                Collections.rotate(permutation, 1);
                ret.add(new ArrayList<T>(permutation));
            }
        }

        // Sort lexicographically
        ret.sort(Combinatorics::compareLists);

        return ret;
    }

    private static <T extends Comparable<? super T>> int compareLists(List<T> a, List<T> b) {
        int N = Math.min(a.size(), b.size());

        for (int i = 0; i < N; i++) {
            int relation = a.get(i).compareTo(b.get(i));
            if (relation == 0) {
                continue;
            }
            // < 0 if a < b,
            // > 0 if a > b
            return relation;
        }
        // If we're here, sizes are not equal.
        // The shorter list is smaller.
        return a.size() - b.size();
    }
}
