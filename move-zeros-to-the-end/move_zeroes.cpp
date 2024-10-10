#include <algorithm>
#include <vector>

std::vector<int> move_zeroes(const std::vector<int>& input) {
  std::vector<int> result = input;
  std::stable_partition(result.begin(), result.end(), [](int x){ return x != 0; });
  return result;
}

auto move_zeroes_neato(std::vector<int> v) {
  stable_partition(begin(v), end(v), std::negate());
  return v;
}