#include <iostream>
using namespace std;

int main()
{
    int t, y, m, d;
    int days[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    cin >> t;

    for (int zzz = 0; zzz < t; zzz++)
    {
        days[2] = 28;
        cin >> y >> m >> d;
        if ((y % 400) == 0 || ((y % 100) != 0 && (y % 4) == 0))
            days[2] = 29;

        y--;
        int total = y * 365 + (y / 4 - y / 100 + y / 400);
        for (int i = 0; i < m; i++)
            total += days[i];
        total += d;

        cout << total % 7 << endl;
    }
}
