#include <iostream>
using namespace std;

int main()
{
    int n, m, a, b, c;
    cin >> n;

    for (int t = 0; t < n; t++)
    {
        cin >> m;
        int arr[m][m];
        a = 0;
        b = m;
        c = ((m - 1) % 4 == 0) ? 0 : 1;
        while (a < b)
        {
            for (int i = a; i < b; i++)
            {
                for (int j = a; j < b; j++)
                {
                    if (c)
                    {
                        arr[i][j] = 1;
                    }
                    else
                    {
                        arr[i][j] = 0;
                    }
                                }
            }
            c = 1 - c;
            a++;
            b--;
        }

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < m; j++)
            {
                cout << arr[i][j];
            }
            cout << endl;
        }
    }
}
