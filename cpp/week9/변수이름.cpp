#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t, c, ipt, answer;
    int check[128] = {0};
    string s;

    for (int i = 48; i < 58; i++)
    {
        check[i] = 2;
    }
    for (int i = 65; i < 91; i++)
    {
        check[i] = 1;
    }
    for (int i = 97; i < 123; i++)
    {
        check[i] = 1;
    }
    check[95] = 1;
    cin >> t;
    for (int zzz = 0; zzz < t; zzz++)
    {
        answer = 1;
        cin >> s;

        if (check[(int)s.at(0)] != 1)
            answer = 0;
        else
        {
            for (int i = 1; i < s.length(); i++)
            {
                if (check[(int)s.at(i)] < 1)
                    answer = 0;
            }
        }

        cout << answer << endl;
    }
}
