#include <iostream>
using namespace std;

int main()
{
    int t, a, b, c, r;
    cin >> t;

    for (int zzz = 0; zzz < t; zzz++)
    {
        cin >> a >> b >> c;
        int arr1[a][b];
        int arr2[b][c];
        // int result[a][c];

        for (int i = 0; i < a; i++)
        {
            for (int j = 0; j < b; j++)
            {
                cin >> arr1[i][j];
            }
        }

        for (int i = 0; i < b; i++)
        {
            for (int j = 0; j < c; j++)
            {
                cin >> arr2[i][j];
            }
        }

        for (int i = 0; i < a; i++)
        { // 3
            for (int j = 0; j < c; j++)
            { // 2
                r = 0;
                for (int l = 0; l < b; l++)
                { // 5
                    r += arr1[i][l] * arr2[l][j];
                }
                cout << r << " ";
            }
            cout << endl;
        }
    }
}
