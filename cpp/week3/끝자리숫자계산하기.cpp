// #include <iostream>
// using namespace std;

// int main() {
//     unsigned int n, m, answer = 1, ipt;
//     cin >> n;

//     for (int t = 0; t < n; t++){
//         cin >> m;
//         for (int i = 0; i < m; i++){
//             cin >> ipt;
//             ipt %= 10;
//             answer = (answer * ipt) % 10;
//         }
//         cout << answer << endl;
//         answer = 1;
//     }
// }

#include <iostream>
using namespace std;

int main()
{
    int count;
    int k, i, j;
    unsigned int b;
    // int b = 1;

    cin >> count;

    for (j = 0; j < count; j++)
    {
        b = 1;
        cin >> i;
        int a[i];

        for (int k = 0; k < i; k++)
        {
            cin >> a[k];
            a[k] %= 10;
            b = (b * a[k]) % 10;
        }

        cout << b << endl;
    }
    return 0;
}