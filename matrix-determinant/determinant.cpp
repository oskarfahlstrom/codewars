#include <vector>
#include <assert.h>

long long determinant(const std::vector<std::vector<long long>>& m) {
    int dim = m.size();

    if (dim == 1) return m[0][0];
    if (dim == 2) return m[0][0] * m[1][1] - m[0][1] * m[1][0];

    long det = 0;
    std::vector<std::vector<long long>> sub(dim - 1, std::vector<long long>(dim - 1));

    for (int x = 0; x < dim; x++) {
        for (int i = 1; i < dim; i++) {
            int sub_j = 0;
            for (int j = 0; j < dim; j++) {
                if (j == x) continue;
                sub[i - 1][sub_j] = m[i][j];
                sub_j++;
            }
        }
        long long sub_det = determinant(sub);
        det += (x % 2 == 0 ? 1 : -1) * m[0][x] * sub_det;
    }
    return det;
}

int main() {
    assert(determinant({{1, 2}, {3, 5}}) == -1);
    return 0;
}
