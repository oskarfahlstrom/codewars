#include <iostream>
#include <cassert>
#include <map>
#include <string>

std::map<char, unsigned> count(const std::string& string) {
    std::map<char, unsigned> r;
    for (char c : string) ++r[c];
    return r;
}


int main() {
    std::string s = "abba";
    std::map<char, unsigned> r = count(s);
    assert(r['a'] == 2);
    assert(r['b'] == 2);   
    return 0;
}
