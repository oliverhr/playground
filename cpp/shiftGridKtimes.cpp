#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> shiftGrid(vector<vector<int>>& grid, const int shift) {
	const int rows = int (grid.size());
	const int cols = int (grid[0].size());

	vector<int> list;
	for (auto& row : grid) {
		list.insert(list.end(), row.begin(), row.end());
	}
	const int length = (int)list.size();
		
	int pos = length - (shift % length);	
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (pos == length) pos = 0;
			grid[i][j] = list[pos++];
		}
	}

	return grid;
}


void printMatrix(vector<vector<int>>& matrix) {
	for (auto& row : matrix) {
		cout << "[";
		for (int col : row) {
			cout << col << ",";
		}
		cout << "]\n";
	}
	cout << "\n";
}


void test1() {
	vector<vector<int>> matrix = {
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	};
	printMatrix(matrix);
	shiftGrid(matrix, 1);
	printMatrix(matrix);
}


void test2() {
	vector<vector<int>> matrix = {
		{ 3, 8,  1,  9},
		{19, 7,  2,  5},
		{ 4, 6, 11, 10},
		{12, 0, 21, 13},
	};
	printMatrix(matrix);
	shiftGrid(matrix, 4);
	printMatrix(matrix);
}


auto main() -> int {
	test1();
	test2();
}
