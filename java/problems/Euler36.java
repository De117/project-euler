package problems;

public class Euler36 {
    /*
    Double-base palindromes
    Problem 36

    The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include leading zeros.)
     */
    public long solution() {
        long sum = 0;
        for (long i = 0; i < 1_000_000; i++) {
            if (isPalindrome(Long.toString(i)) && isPalindrome(Long.toBinaryString(i))) {
                sum += i;
            }
        }
        return sum;
    }

    private boolean isPalindrome(String s) {
        int N = s.length();
        for (int i = 0; i < N/2; i++) {
            if (s.charAt(i) != s.charAt((N - 1) - i)) {
                return false;
            }
        }
        return true;
    }
}
