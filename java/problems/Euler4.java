package problems;

public class Euler4 {

    /*
    Largest palindrome product
    Problem 4

    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
     */
    public long solution() {
        int largestPalindrome = 0;
        for (int i=100; i<1000; i++) {
            for (int j=i+1; j<1000; j++) {
                int candidate = i*j;
                if (candidate > largestPalindrome && isPalindrome(candidate)) {
                    largestPalindrome = candidate;
                }
            }
        }
        return largestPalindrome;
    }

    private boolean isPalindrome(int N) {
        String s = String.format("%d", N);
        int len = s.length();

        for (int i = 0; i < len / 2; i++) {
            if (s.charAt(i) != s.charAt(len - i - 1)) {
                return false;
            }
        }
        return true;
    }
}
