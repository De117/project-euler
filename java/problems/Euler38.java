package problems;

import java.security.cert.CollectionCertStoreParameters;
import java.util.Arrays;
import java.util.Set;
import java.util.TreeSet;
import java.util.stream.Collectors;

public class Euler38 {
    /*
    Pandigital multiples
    Problem 38

    Take the number 192 and multiply it by each of 1, 2, and 3:

        192 × 1 = 192
        192 × 2 = 384
        192 × 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576.
    We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by
    1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is
    the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed
    as the concatenated product of an integer with (1,2, ... , n) where n > 1?
     */
    public long solution() {
        // Let's use m for the integer.
        // We know that n must be small enough to keep the concatenated product
        // nine digits long.
        //
        // For 1 <= m < 10, n <= 9.
        // For 10 <= m < 100, n <= 9/2 = 4
        // For 100 <= m < 1000, n <= 9/3 = 3
        // For 1000 <= m < 10000, n <= 9/4 = 2
        // For m >= 10000, we'd have to concatenate at least two 5-digit
        // numbers, which cannot result in a 9-digit number.
        //
        // So we have only 9999 numbers to check.
        long max = 0;

        for (long m = 1; m < 10000; m++) {
            long bound = (m == 1) ? 9 : (9 / (long)Math.ceil(Math.log10(m)));

            StringBuilder sb = new StringBuilder();
            for (int i = 1; i <= bound; i++) {
                sb.append(String.valueOf(m * i));
            }

            if (sb.length() == 9) {
                Set<Integer> set = sb.chars().boxed().map(c -> c - '0').collect(Collectors.toCollection(TreeSet::new));
                if (set.size() == 9 && !set.contains(0)) {
                    long x = Long.parseLong(sb.toString());
                    if (x > max)
                        max = x;
                }
            }
        }
        return max;
    }
}
