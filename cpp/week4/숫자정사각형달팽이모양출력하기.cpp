#include <iostream>
using namespace std;

int main()
{
    int t, n, start, end, a, b, answer, count;
    cin >> t;

    for (int r = 0; r < t; r++)
    {
        cin >> n >> start >> end;
        int arr[n][n], answ[n * n];

        int num = 1;
        for (int c = 0; c < n; c++)
        {
            for (int d = 0; d < n; d++)
                arr[c][d] = num++;
        }
        count = n - 1;
        a = 0, b = 0, answer = 0;
        while (count > 0)
        {
            for (int i = 0; i < count; i++)
                answ[answer++] = arr[a][b++];
            for (int i = 0; i < count; i++)
                answ[answer++] = arr[a++][b];
            for (int i = 0; i < count; i++)
                answ[answer++] = arr[a][b--];
            for (int i = 0; i < count; i++)
            {
                if (i == count - 1)
                    answ[answer++] = arr[a][b++];
                else
                    answ[answer++] = arr[a--][b];
            }
            count -= 2;
        }
        if (n % 2)
        {
            answ[answer] = arr[n / 2][n / 2];
        }
        for (int i = start - 1; i < end; i++)
            cout << answ[i] << " ";
        cout << endl;
    }
}
