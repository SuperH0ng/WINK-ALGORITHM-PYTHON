#include <iostream>
using namespace std;

int main()
{
    int t, n, num, r, c;
    cin >> t;

    for (int zzz = 0; zzz < t; zzz++)
    {
        num = 1;
        cin >> n;
        r = 0;
        c = n / 2;

        int arr[n][n] = {};

        while (num <= n * n)
        {
            if (arr[r][c] != 0)
            {
                r = (r + 2) % n;
                c = (c + (n - 1)) % n;
            }

            arr[r][c] = num;
            r = (r + (n - 1)) % n;
            c = (c + 1) % n;
            num++;
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cout << arr[i][j] << " ";
            }
            cout << endl;
        }
    }
}
