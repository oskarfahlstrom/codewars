#include <algorithm>
#include <vector>

std::vector<int> move_zeroes(const std::vector<int>& input) {
  std::vector<int> result = input;
  std::stable_partition(result.begin(), result.end(), [](int x){ return x != 0; });
  return result;
}