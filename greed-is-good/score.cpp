// Gordon Gecko -- https://www.codewars.com/kata/5270d0d18625160ada0000e4

#include <vector>
#include <bits/stdc++.h>

const std::map<std::pair<int, int>, int> SCORE_MAP = {
    {{1, 1}, 100},
    {{1, 5}, 50},
    {{3, 1}, 1000},
    {{3, 2}, 200},
    {{3, 3}, 300},
    {{3, 4}, 400},
    {{3, 5}, 500},
    {{3, 6}, 600}}; 

int score(const std::vector<int>& dice) {
    int result = 0;
    for (auto i : {1, 2, 3, 4, 5, 6}) {
        int count = std::count(dice.begin(), dice.end(), i);
        while (count) {
            int lookup = (count >= 3) ? 3 : (count >= 1) ? 1 : 0;
            const auto it = SCORE_MAP.find({lookup, i});
            if (it != SCORE_MAP.end()) {
                result += it->second;
                count -= lookup;
            } else {
                count--;
            }
        }   
    }
    return result;
}