package problems;

import common.Combinatorics;

import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.List;

public class Euler34 {
    /*
    Digit factorials
    Problem 34

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial
    of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
     */
    public long solution() {
        // There must be an upper bound.
        // Adding another digit increases the sum by at most 9! = 362880,
        // but makes the number (up to) eleven times larger.
        //
        // When comparing 10^n to n*9!, we see that after n=5 (five digits),
        // 10^n grows faster, and from n=8 (eight digits) it's also greater.
        //
        // The greatest possible eight-digit sum is 8*9! = 2903040.
        //
        List<Long> numbers = new ArrayList<>();

        for (long i = 3; i < 2_093_040; i++) {
            long sum = 0;
            for (char c : String.valueOf(i).toCharArray()) {
                int digit = c - '0';
                sum += Combinatorics.factorial(digit);
            }
            if (sum == i) {
                numbers.add(i);
            }
        }
        return numbers.stream().reduce(0L, Math::addExact);
    }
}
