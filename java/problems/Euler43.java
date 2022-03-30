package problems;

import common.Combinatorics;
import common.PrimeGenerator;

import java.util.List;
import java.util.stream.Collectors;

public class Euler43 {
    /*
    Sub-string divisibility
    Problem 43

    The number, 1406357289, is a 0 to 9 pandigital number because it is made
    up of each of the digits 0 to 9 in some order, but it also has a rather
    interesting sub-string divisibility property.

    Let d₁ be the 1st digit, d₂ be the 2nd digit, and so on.
    In this way, we note the following:

        d₂d₃d₄=406 is divisible by 2
        d₃d₄d₅=063 is divisible by 3
        d₄d₅d₆=635 is divisible by 5
        d₅d₆d₇=357 is divisible by 7
        d₆d₇d₈=572 is divisible by 11
        d₇d₈d₉=728 is divisible by 13
        d₈d₉d₁₀=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
     */
    public long solution() {
        List<List<Integer>> pandigitals = Combinatorics.permutations(List.of(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
                .stream()
                .filter(l -> l.get(0) != 0)  // filter out those starting with 0
                .collect(Collectors.toList());

        long sum = 0;

        for (List<Integer> digits : pandigitals) {
            boolean hasDivisibilityProperty = true;
            int[] primes = {1, 1, 2, 3, 5, 7, 11, 13, 17};

            for (int i = 2; i <= 8; i++) {
                int subNumber = (digits.get(i-1) * 10 + digits.get(i+1-1)) * 10 + digits.get(i+2-1);
                if (subNumber % primes[i] != 0) {
                    hasDivisibilityProperty = false;
                    break;
                }
            }

            if (hasDivisibilityProperty) {
                sum += digits.stream().mapToLong(i -> i).reduce((acc, digit) -> 10*acc + digit).getAsLong();
            }
        }
        return sum;
    }
}
