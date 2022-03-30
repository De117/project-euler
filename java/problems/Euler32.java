package problems;

import com.sun.source.tree.Tree;
import common.Combinatorics;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.TreeSet;

public class Euler32 {
    /*
    Pandigital products
    Problem 32

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234,
    is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way
          so be sure to only include it once in your sum.
     */
    public long solution() {
        TreeSet<Integer> products = new TreeSet<>();

        // We can generate all 1 through 9 pandigital numbers directly.
        List<List<Integer>> pandigitalNumbers = Combinatorics.permutations(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9));

        for (List<Integer> number : pandigitalNumbers) {
            // Try to divide it in multiple ways.
            //
            // We know that
            //     len(a) + len(b) + len(p) = 9    (where a and b are factors,
            //                                              and p is the product),
            // and in general,
            //     len(a) + len(b) ∈ { len(p), len(p) - 1 }
            //
            // This means that the product can be either 4 or 5 digits long.
            for (int lenP : new int[] {4, 5}) {
                for (int lenA = 1; lenA < (9 - lenP); lenA++) {
                    int lenB = 9 - lenP - lenA;

                    // reconstruct digits
                    int a = number.subList(0, lenA).stream().reduce(0, (acc, digit) -> acc*10 + digit);
                    int b = number.subList(lenA, lenA + lenB).stream().reduce(0, (acc, digit) -> acc*10 + digit);
                    int p = number.subList(lenA + lenB, 9).stream().reduce(0, (acc, digit) -> acc*10 + digit);

                    if (a * b == p) {
                        products.add(p);
                        break;
                    }
                }
            }
        }

        long sum = 0;
        for (long n : products) {
            sum += n;
        }
        return sum;
    }
}
