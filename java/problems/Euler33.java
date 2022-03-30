package problems;

import common.Fraction;

import java.util.ArrayList;
import java.util.List;

public class Euler33 {
    /*
    Digit cancelling fractions
    Problem 33

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
    is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms,
    find the value of the denominator.
     */
    public long solution() {
        List<Fraction> fractions = new ArrayList<>();
        for (int i = 10; i <= 99; i++) {
            for (int j = i+1; j <= 99; j++) {
                if (i % 10 == j % 10 && j % 10 == 0) {
                    // "Trivial" case: both are multiples of 10.
                    continue;
                }
                Fraction f = null;
                if (i % 10 == j / 10    && (j % 10 != 0)) {
                    f = new Fraction(i / 10, j % 10);
                } else if (i / 10 == j % 10    && (j / 10 != 0)) {
                    f = new Fraction(i % 10, j / 10);
                } else if (i / 10 == j / 10    && (j % 10 != 0)) {
                    f = new Fraction(i % 10, j % 10);
                }
                if (f != null && f.equals(new Fraction(i, j))) {
                    fractions.add(f);
                }
            }
        }

        int numeratorProduct = 1;
        int denominatorProduct = 1;
        for (Fraction f : fractions) {
            numeratorProduct *= f.numerator;
            denominatorProduct *= f.denominator;
        }
        return (new Fraction(numeratorProduct, denominatorProduct)).simplified.denominator;
    }
}