package problems;

public class Euler17 {

    /*
    Number letter counts
    Problem 17

    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
          forty-two) contains 23 letters and 115 (one hundred and fifteen)
          contains 20 letters. The use of "and" when writing out numbers is
          in compliance with British usage.
     */

    public long solution() {
        long num = 0;
        for (int i = 1; i <= 1000; i++) {
            num += countLetters(asWord(i));
        }
        return num;
    }

    private int countLetters(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (!Character.isWhitespace(c) && c != '-') {
                count++;
            }
        }
        return count;
    }

    private String asWord(int N) {
        assert N > 0;

        int ones      = (N / 1) % 10;
        int tens      = (N / 10) % 10;
        int hundreds  = (N / 100) % 10;
        int thousands = (N / 1000) % 10;

        String s = "";

        if (thousands > 0) {
            s += ones(thousands) + " thousand ";
        }
        if (hundreds > 0) {
            s += ones(hundreds) + " hundred ";
        }
        if (N % 100 == 0) {
            return s;
        }

        if (!s.equals("")) {
            s += "and ";
        }
        if ((N % 100) <= 20) {
            s += ones(N % 100);
        }
        else if (tens > 0 && ones > 0) {
            s += tens(tens) + "-" + ones(ones);
        }
        else if (tens > 0) {
            s += tens(tens);
        }
        else {
            s += ones(ones);
        }
        return s;
    }

    private String ones(int N) {
        switch (N) {
            case 1: return "one";
            case 2: return "two";
            case 3: return "three";
            case 4: return "four";
            case 5: return "five";
            case 6: return "six";
            case 7: return "seven";
            case 8: return "eight";
            case 9: return "nine";
            case 10: return "ten";
            case 11: return "eleven";
            case 12: return "twelve";
            case 13: return "thirteen";
            case 14: return "fourteen";
            case 15: return "fifteen";
            case 16: return "sixteen";
            case 17: return "seventeen";
            case 18: return "eighteen";
            case 19: return "nineteen";
            case 20: return "twenty";
            default: throw new IllegalArgumentException();
        }
    }

    private String tens(int N) {
        switch (N) {
            case 2: return "twenty";
            case 3: return "thirty";
            case 4: return "forty";
            case 5: return "fifty";
            case 6: return "sixty";
            case 7: return "seventy";
            case 8: return "eighty";
            case 9: return "ninety";
            default: throw new IllegalArgumentException();
        }
    }
}
