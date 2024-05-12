import java.util.HashMap;

public class MostFrequentNumbers {
	public static void main(String[] args) {
		// mostFrequent(array1) should return 1.
        int[] array1 = {1, 3, 1, 3, 2, 1};
        System.out.println(mostFrequent(array1));

        // mostFrequent(array2) should return 3.
        int[] array2 = {3, 3, 1, 3, 2, 1};
        System.out.println(mostFrequent(array2));

        // mostFrequent(array3) should return null.
        int[] array3 = {};
        System.out.println(mostFrequent(array3));

        // mostFrequent(array4) should return 0.
        int[] array4 = {0};
        System.out.println(mostFrequent(array4));

        // mostFrequent(array5) should return -1.
        int[] array5 = {0, -1, 10, 10, -1, 10, -1, -1, -1, 1};
        System.out.println(mostFrequent(array5));
	}

	private static Integer mostFrequent(int[] givenArray) {
		HashMap<Integer, Integer> historic = new HashMap<>();
		HashMap<String, Integer> maxItem = new HashMap<>();

		maxItem.put("number", null);
		maxItem.put("apperances", 0);

		for (Integer number: givenArray) {
			Integer counter = historic.getOrDefault(number, 0) + 1;
			if (maxItem.get("apperances") < counter) {
				maxItem.put("number", number);
				maxItem.put("apperances", counter);
			}
			historic.put(number, counter);
		}

		return maxItem.get("number");
	}
}
