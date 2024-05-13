#include <iostream>
#include <type_traits>

#include <unordered_set>


#define _n "\n"

bool valid (std::string, std::string);

int main() {
    valid("eleven plus two", "twelve plus one");
}


bool valid(std::string original, std::string anagram) {
    if (anagram.length() != anagram.length()) return false;

    std::unordered_set<char> chars;
    std::unordered_multiset<char> org;
    std::unordered_multiset<char> ana;

    for (uint i = 0; i < anagram.length(); i++) {
        chars.insert(original[i]);
        org.insert(original[i]);
        ana.insert(anagram[i]);
    }

    for (auto ch : chars) {
        if (!ana.contains(ch)) return false; // -std=c++20
        if (ana.count(ch) != org.count(ch)) return false;
    }

    return true;
}
