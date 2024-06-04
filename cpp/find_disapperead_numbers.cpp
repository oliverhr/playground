#include <iostream>
#include <vector>

using namespace std;

vector<int> findDisappereadNumbers(const vector<int> &numbers) {
    vector<int> disappeared;
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
