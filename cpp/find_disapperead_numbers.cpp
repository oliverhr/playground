#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

vector<int> findDisappereadNumbers(const vector<int> &numbers) {
    vector<int> disappeared(numbers.size());
    std::iota(disappeared.begin(), disappeared.end(), 1);

    for (int i = 0; i < numbers.size(); i++ ) {
        cout << numbers[i] << ",";
    }
    cout << "\n";
    return disappeared;
}

void printArray(vector<int> &numbers) {
    for (int num : numbers) {
        cout << num << ",";
    }
    cout << "\n";
}

void test1() {
    vector<int> nums = {4, 3, 2, 7, 8, 2, 3, 1};
    printArray(nums);
    vector<int> missing = findDisappereadNumbers(nums);
    printArray(missing);
}

auto main(int argc, const char *argv[]) -> int {
    test1();
}
