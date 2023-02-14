#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int t, c, a1, a2, b1, b2, M, m;
    bool overlap;
    cin >> t;

    for (int zzz = 0; zzz < t; zzz++)
    {
        cin >> a1 >> a2 >> b1 >> b2;
        M = max(a2, b2);
        m = min(a1, b1);

        // overlap
        if (M - m < a2 - a1 + b2 - b1)
            overlap = true;
        else
            overlap = false;

        if (overlap)
            cout << a2 - a1 + b2 - b1 - (M - m) << " " << M - m << endl;
        else
            cout << 0 << " " << a2 - a1 + b2 - b1 << endl;
    }
}
