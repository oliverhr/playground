#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

vector<int> findDisappereadNumbers(const vector<int> &numbers) {
    int size = numbers.size();

    vector<bool> exist(size + 1, false);
    for (auto &num : numbers) {
        exist[num] = true;
    }

    vector<int> disappeared;
    for (int i = 1; i <= size; i++) {
        if (!exist.at(i))
            disappeared.push_back(i);
    }

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

void test2() {
    vector<int> nums = {1, 1};
    printArray(nums);
    vector<int> missing = findDisappereadNumbers(nums);
    printArray(missing);
}

auto main(int argc, const char *argv[]) -> int {
    test1();
    test2();
}
