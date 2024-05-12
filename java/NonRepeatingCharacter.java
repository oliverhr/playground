import java.util.HashMap;

public class NonRepeatingCharacter {
    public static void main(String[] args) {
        test();
    }

    private static void test() {
        System.out.println(nonRepeating("abcab")); // should return 'c'
        System.out.println(nonRepeating("abab")); // should return null
        System.out.println(nonRepeating("aabbbc")); // should return 'c'
        System.out.println(nonRepeating("aabbdbc")); // should return 'd'
    }

    public static Character nonRepeating(String string) {
        HashMap<Character, Integer> mem = new HashMap<>();

        for (int i = 0; i < string.length(); i++) {
            char ch = string.charAt(i);
            if (mem.containsKey(ch)) mem.put(ch, mem.get(ch) + 1);
            else mem.put(ch, 1);
        }

        for (char ch: string.toCharArray())
            if (mem.get(ch) == 1) return ch;

        return null;
    }
}
