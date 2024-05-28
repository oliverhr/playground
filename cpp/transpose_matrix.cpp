#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> transpose(const vector<vector<int>>& matrix)
{
	int rows = (int) matrix.size();
	int cols = (int) matrix[0].size();

	vector<vector<int>> changed(rows, vector<int>(cols));

	for (int r = 0; r < rows; r++) {
		for (int c = 0; c < cols; c++) {
			changed[c][r] = matrix[r][c];
		}
	}
	return changed;
}

void printMatrix(vector<vector<int>>& matrix)
{
	for (auto& row : matrix) {
		cout << "[";
		for (int col : row) {
			cout << col << ",";
		}
		cout << "]\n";
	}
	cout << endl;
}


void test1()
{
	vector<vector<int>> matrix = {
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9}
	};
	cout << "Original:" << endl;
	printMatrix(matrix);

	cout << "Transposed:" << endl;
	auto result = transpose(matrix);
	printMatrix(result);
}


int main()
{
	test1();
}
