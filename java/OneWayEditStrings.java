public class OneWayEditStrings {

    private static final int MAX_DIFF = 1;

    public static void main(String[] args) {
       // same length
        test("a",       "a",      true);  // 1 equal then true
        test("abcdef",  "abqdef", true);  // 2
        test("abcdef",  "abccef", true);  // 3
        test("aaa",     "abc",    false); // 4 diff chars >= 2
        test("abc",     "bcc",    false); // 5 diff chars >= 2

        // different length
        test("abc",     "abcde",  false); // 6 length diff >= 2
        test("abcde",   "abc",    false); // 7 length diff >= 2

        // String1 has less chars
        test("bcde",    "abcde",  true);  // 10 rem e from the left
        test("abde",    "abcde",  true);  // 10 rem c in the middle
        test("abcd",    "abcde",  true);  // 10 rem e from the right

        // String1 has more chars
        test("abcdef",  "bcdef",  true);  // 8 add a to the left
        test("abcde",   "abce",   true);  // 9 add c in the middle
        test("abcdef",  "abcde",  true);  // 8 add f to the right
    }

    private static void test(String base, String extra, boolean expected) {
        Boolean result = isOneAway(base, extra);
        System.out.printf("%s <-> %s, Passed: %B\n", base, extra, result == expected);
    }

    private static Boolean sameLength(String base, String extra) {
        int counter = 0;
        for (int i = 0; i < base.length(); i++) {
            if (base.charAt(i) != extra.charAt(i)) {
                counter++;
                if (counter > MAX_DIFF) return false;
            }
        }
        return true;
    }

    private static Boolean differentLength(String smaller, String bigger) {
        int counter = 0;
        for (int i = 0; i < bigger.length(); i++) {
            if (smaller.charAt(i + counter) != bigger.charAt(i)) {
                counter++;
                if (counter > MAX_DIFF) return false;
            }
        }
        return true;
    }

    public static Boolean isOneAway(String base, String extra) {
        if (base == extra) return true;
        if (java.lang.Math.abs(base.length() - extra.length()) > MAX_DIFF) return false;

        if (base.length() == extra.length()) return sameLength(base, extra);
        return (base.length() > extra.length())
            ? differentLength(base, extra)
            : differentLength(extra, base);
    }
}

