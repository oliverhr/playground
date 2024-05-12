# include <iostream>

using namespace std;

int main()
{
	int scores[] = {90, 70, 50, 80, 60, 85};

	int length = sizeof(scores) / sizeof(scores[0]);

	int temp[length + 1];

	for (int i = 0; i < length; i++)
	{
        if (i >= 2) {
            temp[i+1] = scores[i];
        } else {
            temp[i] = scores[i];
        }
	}
	temp[2] = 75;

	memcpy(scores, temp, sizeof(temp));

	for (int i = 0; i < length + 1; i++)
	{
		cout << scores[i] << ",";
	}

	return 0;
}

