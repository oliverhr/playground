import java.util.ArrayList;
import java.util.Arrays;

public class CommonElementsInTwoTortedArrays {
    public static void main(String[] args) {
        testImplementation();
    }

    private static void testImplementation() {
        // should return [1, 4, 9].
        int[] array1a = {1, 3, 4, 6, 7, 9};
        int[] array1b = {1, 2, 4, 5, 9, 10};
        System.out.println(Arrays.toString(commonElements(array1a, array1b)));

        // should return [1, 2, 9, 10, 12].
        int[] array2a = {1, 2, 9, 10, 11, 12};
        int[] array2b = {0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15};
        System.out.println(Arrays.toString(commonElements(array2a, array2b)));

        // should return [1, 2, 4, 5].
        int[] array3a = {0, 1, 2, 3, 4, 5};
        int[] array3b = {1, 2, 4, 5, 9, 10};
        System.out.println(Arrays.toString(commonElements(array3a, array3b)));

        // should return [].
        int[] array4a = {0, 1, 2, 3, 4, 5};
        int[] array4b = {6, 7, 8, 9, 10, 11};
        System.out.println(Arrays.toString(commonElements(array4a, array4b)));
    }

    public static Integer[] commonElements(int[] arrayA, int[] arrayB) {
        ArrayList<Integer> result = new ArrayList<>();
        int a = 0;
        int b = 0;

        while(a < arrayA.length && b < arrayB.length) {
            if (arrayA[a] == arrayB[b]) {
                result.add(arrayA[a]);
                a++; b++;
            }
            else if (arrayA[a] < arrayB[b]) a++;
            else if (arrayA[a] > arrayB[b]) b++;
        }

        return result.toArray(new Integer[result.size()]);
    }
}
