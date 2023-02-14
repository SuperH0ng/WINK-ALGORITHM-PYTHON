#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int t, c, s1[4], s2[4], s1s, s2s, s1xl, s2xl, s1yl, s2yl, Mx, mx, My, my;
    bool overlap;
    cin >> t;

    for (int zzz = 0; zzz < t; zzz++)
    {
        cin >> s1[0] >> s1[1] >> s1[2] >> s1[3];
        cin >> s2[0] >> s2[1] >> s2[2] >> s2[3];
        s1xl = s1[2] - s1[0];
        s2xl = s2[2] - s2[0];
        s1yl = s1[3] - s1[1];
        s2yl = s2[3] - s2[1];
        s1s = s1xl * s1yl;
        s2s = s2xl * s2yl;
        Mx = max(s1[2], s2[2]);
        mx = min(s1[0], s2[0]);
        My = max(s1[3], s2[3]);
        my = min(s1[1], s2[1]);

        // overlap
        if ((Mx - mx < s1xl + s2xl) && (My - my < s1yl + s2yl))
            overlap = true;
        else
            overlap = false;

        if (overlap)
        {
            cout << s1s + s2s - (((s1xl + s2xl) - (Mx - mx)) * ((s1yl + s2yl) - (My - my)));
            cout << " " << 2 * (Mx - mx + My - my) << endl;
        }
        else
        {
            cout << s1s + s2s << " " << 2 * (s1xl + s2xl + s1yl + s2yl) << endl;
        }
    }
}
