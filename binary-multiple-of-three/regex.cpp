// https://www.codewars.com/kata/54de279df565808f8b00126a

#include <string>
#include <regex>
#include <assert.h>

// https://math.stackexchange.com/questions/140283/why-does-this-fsm-accept-binary-numbers-divisible-by-three
const std::string multiple_of_3_regex = "^(0|(1(01*0)*1))*$";

int main() {
    std::regex solution(multiple_of_3_regex);
    assert(std::regex_match(" 0", solution) == false);
    assert(std::regex_match("abc", solution) == false);
    assert(std::regex_match("000", solution) == true);
    return 0;
}