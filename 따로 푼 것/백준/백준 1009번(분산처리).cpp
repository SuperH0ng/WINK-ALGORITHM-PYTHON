#include <iostream>
using namespace std;

int main()
{
    int t, a, b, count;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> a >> b;
        count = 1;
        for (int j = 0; j < b; j++)
        {
            count = (count * a) % 10;
        }
        if (!(count))
        {
            count = 10;
        }
        cout << count << endl;
    }
}