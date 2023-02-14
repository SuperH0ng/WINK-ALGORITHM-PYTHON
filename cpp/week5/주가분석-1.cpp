#include <iostream>
using namespace std;

int main()
{
    int t, c, ipt, day, now, answer;
    bool check;
    cin >> t;

    for (int zzz = 0; zzz < t; zzz++)
    {
        answer = 0;
        check = false;
        cin >> day;
        cin >> now;
        for (int i = 1; i < day; i++)
        {
            cin >> ipt;
            if (ipt < now)
            {
                if (check)
                {
                    answer += 1;
                }
                check = false;
            }
            else if (ipt > now)
            {
                check = true;
            }
            now = ipt;
        }
        cout << answer << endl;
    }
}
