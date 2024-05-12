#include <iostream>
#include <type_traits>

#include <set>
#include <unordered_map>
#include <tuple>
#include <ranges>


#define _n "\n"

bool valid (std::string, std::string);

int main() {
    valid("eleven plus two", "twelve plus one");
}


bool valid(std::string original, std::string anagram) {
    if (anagram.length() != anagram.length()) return false;
    int const len = anagram.length(); // automatic casting

    // just for fun
    std::set<char> chars(original.begin(), original.end());

    // value isn't necessary but, the index is being saved
    std::unordered_map<char, int> org;
    std::unordered_map<char, int> ana;

    // note: check c++23 std::views::zip
    for (int i = 0; i < len; i++) {
        org[original[i]] = i;
        ana[anagram[i]] = i;
    }

    for (auto ch : chars) {
        if (!ana.contains(ch)) return false;    // -std=c++20
        if (ana.count(ch) != org.count(ch)) return false;
    }

    return true;
}
