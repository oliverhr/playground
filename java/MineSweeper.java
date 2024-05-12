public class MS {
    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.

        System.out.println("should return:");
        System.out.println("  0  1 -1");
        System.out.println("  1  2  1");
        System.out.println(" -1  1  0");

        int[][] bombs1 = {{0, 2}, {2, 0}};

        int[][] board1 = mineSweeper(bombs1, 3, 3);
        System.out.println("\n");

        System.out.println("Returned:");
        for (int[] row : board1) {
            for (int cell : row) {
                System.out.printf("%3d", cell);
            }
            System.out.println();
        }

        // int[][] bombs2 = {{0, 0}, {0, 1}, {1, 2}};
        // mineSweeper(bombs2, 3, 4) should return:
        // [[-1, -1, 2, 1],
        //  [2, 3, -1, 1],
        //  [0, 1, 1, 1]]

        // int[][] bombs3 = {{1, 1}, {1, 2}, {2, 2}, {4, 3}};
        // mineSweeper(bombs3, 5, 5) should return:
        // [[1, 2, 2, 1, 0],
        //  [1, -1, -1, 2, 0],
        //  [1, 3, -1, 2, 0],
        //  [0, 1, 2, 2, 1],
        //  [0, 0, 1, -1, 1]]
    }

    public static int[][] mineSweeper(int[][] bombs, int numRows, int numCols) {
        int[][] field = new int[numRows][numCols];

        for (int[] bomb: bombs) {
            int rowIndex = bomb[0];
            int colIndex = bomb[1];

            field[rowIndex][colIndex] = -1;

            for (int r = rowIndex - 1; r <= rowIndex + 1; r++) {
                if (r < 0 || r >= numRows ) continue;
                for (int c = colIndex - 1; c <= colIndex + 1; c++) {
                if (r < 0 || r >= numRows ) continue;
                    if (c >= 0 && c < numCols && field[r][c] != -1)
                        field[r][c]++;
                }
            }
        }
        return field;
    }

    public static int[][] click(int[][] field, int numRows, int numCols, int givenI, int givenJ) {
        return field;
    }
}

