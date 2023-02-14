#include <iostream>
#include <cmath>
using namespace std;

int pow(int n, int l);

int main()
{
    int t, n, m, s;
    unsigned int sum;
    cin >> t;

    for (int c = 0; c < t; c++)
    {
        cin >> n;
        int arr[10] = {};
        sum = 0;
        m = n;
        s = 0;
        while (m > 0)
        {
            arr[s] = m % 10;
            m /= 10;
            s++;
        }

        for (int i = 0; i < 10; i++)
        {
            sum += pow(arr[i], s);
        }

        if (sum == n)
            cout << 1 << endl;
        else
            cout << 0 << endl;
    }
}

int pow(int n, int l)
{
    int result = 1;
    while (l > 0)
    {
        result *= n;
        l--;
    }
    return result;
}