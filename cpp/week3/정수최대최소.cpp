#include <iostream>
using namespace std;

int main() {
    int n, m, ipt, max, min;
    cin >> n;
    
    for (int t = 0; t < n; t++){
        cin >> m;
        max = -2147483648, min = 2147483647;
        for (int i = 0; i < m; i++){
            cin >> ipt;
            if (ipt > max) {
                max = ipt;
            }
            if (ipt < min) {
                min = ipt;
            }
        }
        cout << max << " " << min << endl;
    }
}
