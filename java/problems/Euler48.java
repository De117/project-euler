package problems;

import java.math.BigInteger;

public class Euler48 {
    /*
    Self powers
    Problem 48

    The series, 1² + 2² + 3³ + ... + 10¹⁰ = 10405071317.

    Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.
     */
    public long solution() {
        BigInteger sum = BigInteger.ZERO;
        for (int i=1; i <= 1000; i++) {
            sum = sum.add(BigInteger.valueOf(i).pow(i));
        }
        String s = sum.toString();
        return Long.parseLong(s.substring(s.length() - 10));
    }
}
