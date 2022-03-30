package problems;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Euler42 {
    /*
    Coded triangle numbers
    Problem 42

    The nth term of the sequence of triangle numbers is given by, t_n = n(n+1)/2;
    so the first ten triangle numbers are:

        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value.
    For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10.
    If the word value is a triangle number then we shall call the
    word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'),
    a 16K text file containing nearly two-thousand common
    English words, how many are triangle words?
     */

    private final String FILENAME = "p042_words.txt";

    public long solution() {
        // We only need a small subset of triangle numbers.
        Set<Integer> triangleNumbers = new HashSet<>();
        for (int n = 1; n < 100; n++) {
            triangleNumbers.add(n * (n + 1) / 2);
        }

        int numTriangleWords = 0;
        try {
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(
                        new FileInputStream(FILENAME)
                    )
            );
            String line = reader.readLine();
            for (String word : line.split(",")) {
                word = word.substring(1, word.length() - 1);  // strip quotes

                int value = 0;
                for (char c : word.toCharArray()) {
                    value += c - 'A' + 1;
                }

                if (triangleNumbers.contains(value)) {
                    numTriangleWords++;
                }
            }
        } catch (IOException e) {
            System.out.printf("Caught IOException: %s\n", e.getMessage());
            System.exit(1);
        }
        return numTriangleWords;
    }
}
