class SortableArray:

    def __init__(self, array):
        self.array = array


    def partition(self, left_pointer, right_pointer):
        # For this case, the right-most element is being choosed
        # as the pivot, the index of the pivot is being keep
        # for later use:
        pivot_index = right_pointer

        # grab the pivot value itself:
        pivot = self.array[pivot_index]

        # We start the right pointer immediately to the left of the pivot
        right_pointer -= 1

        while True:
            # Move the left pointer to the right as long as it
            # points to value that is less than the pivot:
            while self.array[left_pointer] < pivot:
                left_pointer += 1

            # Move the right pointer to the left as long as it
            # points to a value that is greater than the pivot:
            while self.array[right_pointer] > pivot:
                right_pointer -= 1

            #              *------>.<------*

            # We've now reached the point where we've stopped
            # moving both the left and right pointers, check
            # whether the left pointer has reached or gone
            # beyond the right pointer. If it has, "break out"
            # of the loop so we can swap the pivot later on
            # in our code:
            if left_pointer >= right_pointer: break

            # If the left pointer is still to the left of the right pointer,
            # swap the values of the left and right pointers:
            self.swap(left_pointer, right_pointer)

            # We move the left pointer over to the right, gearing up
            # for the next round of left and right pointer movements:
            left_pointer += 1

        # As the final step of the partition, we swap the value
        # of the left pointer with the pivot:
        self.swap(left_pointer, pivot_index)

        # We return the left_pointer for the sake of the quicksort method
        # which will appear later in this chapter:
        return left_pointer



    # QUICK SORT
    def quicksort(self, left_index, right_index):
        if right_index - left_index <= 0: return

        # Get a number to use as pivot the use the index
        pivot_index = self.partition(left_index, right_index)

        self.quicksort(left_index, pivot_index - 1)
        self.quicksort(pivot_index + 1, right_index)


    # QUICK SELECT
    def quickselect(self, kth_lowest_value, left_index, right_index):
        if right_index - left_index <= 0:
            return self.array[left_index]

        pivot_index = self.partition(left_index, right_index)

        if kth_lowest_value < pivot_index:
            return self.quickselect(kth_lowest_value, left_index, pivot_index - 1)
        elif kth_lowest_value > pivot_index:
            return self.quickselect(kth_lowest_value, pivot_index + 1, right_index)
        else:
            return self.array[pivot_index]


    def swap(self, left_pointer, right_pointer):
        left_value = self.array[left_pointer]
        right_value = self.array[right_pointer]
        self.array[right_pointer] = left_value
        self.array[left_pointer] = right_value


array: list[int] = [0, 5, 2, 1, 6, 3]
qs = SortableArray(array)
qs.quicksort(0, len(array) - 1)
print(qs.array)
