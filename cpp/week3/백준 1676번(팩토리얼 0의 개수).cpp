#include <iostream>
#include <algorithm>
using namespace std;

int main()
{

    int n, count2 = 0, count5 = 0, copyI;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        copyI = i;
        while (!(copyI % 2))
        {
            copyI /= 2;
            count2++;
        }
        while (!(copyI % 5))
        {
            copyI /= 5;
            count5++;
        }
    }

    cout << min(count2, count5) << endl;
}
