#include <iostream>
using namespace std;

int main() {
    int n, a, b, c, d, e, f;
    cin >> n;

    for (int t = 0; t < n; t++){
        cin >> a >> b >> c;

        if (a <= b) {
            if (b <= c) {
                d = a;
                e = b;
                f = c;
            }else {
                if (a <= c) {
                    d = a;
                    e = c;
                    f = b;
                }else {
                    d = c;
                    e = a;
                    f = b;
                }
            }
        }else {
            if ( c<=b) {
                d = c;
                e = b;
                f = a;
            }else {
                if ( a <= c) {
                    d = b;
                    e = a;
                    f = c;
                }else {
                    d = b;
                    e = c;
                    f = a;
                }
            }
        }

        cout << d << " " << e << " " << f << endl;

    }
}
