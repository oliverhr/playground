#include <iostream>

using namespace std;


void swap(int arr[], int index)
{
	int temp = arr[index];

	arr[index] = arr[index + 1];
	arr[index + 1] = temp;
}


void bubble(int arr[], int length)
{
	for (int i = 0; i < length - 1; i++)
	{
		for (int j = 0; j < length - 1 - i; j++)
		{
			if (arr[j] > arr[j + 1]) swap(arr, j);
		}
	}
}


void print(int arr[], int length)
{
	for (int i = 0; i < length; ++i)
	{
		cout << arr[i] << " ";
	}
	cout << "\n";

}


int main(int argc, char const *argv[])
{
	int arr[] = {90, 70, 50, 80, 60, 85};
	int length = sizeof(arr) / sizeof(arr[0]);

	bubble(arr, length);
	print(arr, length);

	return 0;
}

