// #include <iostream>
// using namespace std;

// int main() {
//     int n;;
//     double answer, h, m;
//     cin >> n;

//     for (int t = 0; t < n; t++){
//         cin >> h >> m;
//         double ha = (h / 12) * 360 + (30 * m) / 60;
//         double ma = (m / 60) * 360;

//         if (ma >= ha) {
//             answer = ma - ha;
//         }else {
//             answer = ha - ma;
//         }

//         if (answer > 180) {
//             answer = 360 - answer;
//         }

//         cout << (int) answer << endl;
//     }
// }


// #include <iostream>
// #include <math.h>
// #include <cmath>

// using namespace std;
// int main(void)
// {
//     int t;
//     int h, m;
//     cin >> t;
//     for(int i=0; i<t; i++)
//     {
//         cin >> h >> m;

//         double a = abs(30 * h);
//         double b = abs(5.5 * m);


//         if (a>b)
//             cout << trunc(a-b) << endl;
//         else
//             cout << trunc(b-a) << endl;
            
//         }
// return 0; 
// }


#include <iostream>
#include <math.h>
#include <cmath>

using namespace std;
int main(void)
{
    int t;
    int h, m;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        cin >> h >> m;

        double a = abs(30 * h + 0.5 * m);
        double b = abs(6 * m);

        double clock = abs(a-b);

        if (clock > 180)
            cout << trunc(360 - clock) << endl;
        else
            cout << trunc(clock) << endl;

        }
return 0; 
}