#include <vector>
#include <assert.h>

long determinant(const std::vector<std::vector<long>>& matrix) {
    int dim = matrix.size();

    if (dim == 1) 
        return matrix[0][0];
    if (dim == 2)
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];

    long det = 0;
    std::vector<std::vector<long>> submatrix(dim - 1, std::vector<long>(dim - 1));

    for (int x = 0; x < dim; x++) {
        for (int i = 1; i < dim; i++) {
            int sub_j = 0;
            for (int j = 0; j < dim; j++) {
                if (j == x)
                    continue;
                submatrix[i - 1][sub_j] = matrix[i][j];
                sub_j++;
            }
        }

        long sub_det = determinant(submatrix);
        det += (x % 2 == 0 ? 1 : -1) * matrix[0][x] * sub_det;
    }
    return det;
}

int main() {
    assert(determinant({{1, 2}, {3, 5}}) == -1);
    return 0;
}
