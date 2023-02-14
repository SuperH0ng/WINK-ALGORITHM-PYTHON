#include <iostream>
using namespace std;

int main()
{
    int t, c, ipt, answer;
    cin >> t;

    for (int k = 0; k < t; k++)
    {
        cin >> c;
        for (int i = 0; i < c; i++)
        {
            for (int j = 0; j < c; j++)
            {
                // + 인 줄
                if (i == 0 or i == c / 2 or i == c - 1)
                {
                    if (i == c / 2 and j == c / 2)
                    {
                        cout << '*';
                    }
                    else if (j == 0 or j == c / 2 or j == c - 1)
                    {
                        cout << '+';
                    }
                    else
                    {
                        cout << '-';
                    }
                }
                // + 아닌 줄
                else
                {
                    if (j == 0 or j == c / 2 or j == c - 1)
                    {
                        cout << '|';
                    }
                    else if (i == j)
                    {
                        cout << '\\';
                    }
                    else if (i + j == c - 1)
                    {
                        cout << '/';
                    }
                    else
                    {
                        cout << '.';
                    }
                }
            }
            cout << endl;
        }
    }
}
