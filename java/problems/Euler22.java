package problems;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class Euler22 {

    /*
    Names scores
    Problem 22

    Using names.txt (right click and 'Save Link/Target As...'), a 46K text
    file containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
    So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
     */
    public long solution() {

        // Read the names in
        ArrayList<String> names = new ArrayList<String>();
        try {
            BufferedReader reader = new BufferedReader(new FileReader("p022_names.txt"));
            String[] quotedNames = reader.readLine().split(",");
            for (String name : quotedNames) {
                name = name.substring(1, name.length() - 1);
                names.add(name);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        Collections.sort(names);

        long sum = 0;
        for (int i = 0; i < names.size(); i++) {
            sum += nameValue(names.get(i)) * (i+1);
        }

        return sum;
    }

    private long nameValue(String name) {
        long value = 0;
        for (char c : name.toCharArray()) {
            value += c - 'A' + 1;
        }
        return value;
    }
}
