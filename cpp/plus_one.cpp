/* ----------------------------------------------------------------------------
Title: Plus One

Description:
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.

The digits are ordered from most significant to least significant in
left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Constraints:
  ∙ 1 <= digits.length <= 100
  ∙ 0 <= digits[i] <= 9
  ∙ digits does not contain any leading 0's.

---------------------------------------------------------------------------- */

#include <iostream>
#include <vector>


void printVector(std::vector<int>& digits)
{
	for (auto n : digits)
	{
		std::cout << n;
	}
	std::cout << "\n";
}


// ----------------------------------------------------------------------------
std::vector<int> plusOne(std::vector<int>& digits)
{
	int length = digits.size();
	if (digits.at(length - 1) != 9)
	{
		digits[length - 1]++;
		return digits;
	}

	int counter = 0;
	for (int i = length - 1; i >= 0; i--)
	{
		if (digits.at(i) != 9) break;
		counter++;
	}

	if (counter < length)
	{
		int idx = (length - 1) - counter;
		digits[idx]++;

		for (int i = idx + 1; i < digits.size(); i++)
		{
			digits[i] = 0;
		}
		return digits;
	}

	// Only nines
	digits.insert(digits.begin(), 1);
	std::vector<int>::iterator iter = digits.begin();
	for (iter++; iter < digits.end(); iter++)
	{
		*iter = 0;
	}
	return digits;
}


// ----------------------------------------------------------------------------
void test1()
{
	std::vector<int> digits = { 4, 3, 2, 1 };
	plusOne(digits);
	printVector(digits);
}

void test2()
{
	std::vector<int> digits = { 9 };
	plusOne(digits);
	printVector(digits);
}

void test3()
{
	std::vector<int> digits = { 1, 9 };
	plusOne(digits);
	printVector(digits);
}

void test4()
{
	std::vector<int> digits = { 1, 9, 9 };
	plusOne(digits);
	printVector(digits);
}

// ----------------------------------------------------------------------------
int main()
{
	test1();
	test2();
	test3();
	test4();
}
