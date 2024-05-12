public class ArrayIsARotation {
    public static void main(String[] args) {
        test();
    }

    private static void test() {
        Boolean result;
        int[] baseArray = {1, 2, 3, 4, 5, 6, 7};

        // should return true.
        result = isRotation(baseArray, new int[]{4, 5, 6, 7, 1, 2, 3});
        System.out.println(result + "\n");

        // should return false.
        result = isRotation(baseArray, new int[]{4, 5, 6, 7, 8, 1, 2, 3});
        System.out.println(result + "\n");

        // should return false.
        result = isRotation(baseArray, new int[]{4, 5, 6, 9, 1, 2, 3});
        System.out.println(result + "\n");

        // should return false.
        result = isRotation(baseArray, new int[]{4, 6, 5, 7, 1, 2, 3});
        System.out.println(result + "\n");

        // should return false.
        result = isRotation(baseArray, new int[]{4, 5, 6, 7, 0, 2, 3});
        System.out.println(result + "\n");

        // should return true.
        result = isRotation(baseArray, new int[]{7, 1, 2, 3, 4, 5, 6});
        System.out.println(result + "\n");

        // should return true.
        result = isRotation(baseArray, new int[]{1, 2, 3, 4, 5, 6, 7});
        System.out.println(result + "\n");
    }

    public static Boolean isRotation(int[] base, int[] rotated) {
        if (base.length != rotated.length) return false;

        final int length = base.length;
        final int diff = rotated[0] - base[0];
        final int span = (diff == 0) ? diff : length - diff;

         System.out.println(java.util.Arrays.toString(base));
         System.out.println(java.util.Arrays.toString(rotated));
         System.out.printf("Length: %d, Diff: %d, Span: %d\n", length, diff, span);

        if (base[0] != rotated[span]) return false;

        for (int i = 0; i < length; i++) {
            int j = (span + i) % length;
            System.out.printf("(%d + %d) %% %d = %d\n", span, i, length, j);

            if (base[i] != rotated[j]) return false;
        }

        return true;
    }
}
