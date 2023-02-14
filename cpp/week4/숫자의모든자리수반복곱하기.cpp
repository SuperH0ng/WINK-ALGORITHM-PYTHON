#include <iostream>
using namespace std;

int main()
{
    int t;
    unsigned int n, answer;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> n;
        answer = n;

        while (answer > 9)
        {
            answer = 1;
            while (n > 0)
            {
                if (n % 10)
                {
                    answer *= (n % 10);
                }
                n /= 10;
            }
            n = answer;
        }
        cout << answer << endl;
    }
}

// int num2 = stoi(s);
// string s2 = to_string(num);
