#include <iostream>
#include <vector>

using namespace std;

bool validMountainArray(const vector<int> &array) {
    if (array.size() < 3)  return false;

    const int length = (int)array.size() - 1;
    int peak = 0;

    while (peak < length && array[peak] < array[peak + 1]) {
        peak++;
    }
    if (peak == 0 || peak == length) return false;

    while (peak < length && array[peak] > array[peak + 1]) {
        peak++;
    }
    return peak == length;
}

void test1() {
    vector<int> array = {0, 2, 3, 4, 5, 2, 1, 0};
    string isValid = validMountainArray(array) ? "Yes" : "No";
    cout << "Is a valid mountain array?: " << isValid << endl;
}

void test2() {
    vector<int> array = {1, 2};
    string isValid = validMountainArray(array) ? "Yes" : "No";
    cout << "Is a valid mountain array?: " << isValid << endl;
}

void test3() {
    vector<int> array = {3, 4, 5};
    string isValid = validMountainArray(array) ? "Yes" : "No";
    cout << "Is a valid mountain array?: " << isValid << endl;
}

void test4() {
    vector<int> array = {0, 3, 2, 1};
    string isValid = validMountainArray(array) ? "Yes" : "No";
    cout << "Is a valid mountain array?: " << isValid << endl;
}

auto main(int argc, const char *argv[]) -> int {
    test1();
    test2();
    test3();
    test4();
}
