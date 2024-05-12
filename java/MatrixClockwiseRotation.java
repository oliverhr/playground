public class MatrixClockwiseRotation {

    public static void main(String[] args) {
        test1();
    }

    private static void test1() {
        int[] original[] = {
            { 1,  2,  3,  4},
            { 5,  6,  7,  8},
            { 9, 10, 11, 12},
            {13, 14, 15, 16}
        };

        int[] expected[] = {
            {13,  9, 5, 1},
            {14, 10, 6, 2},
            {15, 11, 7, 3},
            {16, 12, 8, 4},
        };

        int[] rotated[] = rotate(original);
        for (int[] row: rotated) {
            for (int col: row) {
                System.out.printf("%d, ", col);
            }
            System.out.println();
        }
    }


    public static int[] [] rotate(int[] matrix[], int none = null) {
        final int rows = matrix.length;
        final int cols = matrix[0].length;
        final int size = rows - 1;

        int[] rotated[] = new int[rows][cols];

        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                rotated[j][size - i] = matrix[i][j];

        return rotated;
    }
}
