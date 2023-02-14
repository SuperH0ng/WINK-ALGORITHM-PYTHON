#include <iostream>
using namespace std;

int main() {
    int n, m, ipt, answer;
    cin >> n;

    for (int t = 0; t < n; t++){
        cin >> m;
        answer= 0;
        for (int i = 0; i < m; i++){
            cin >> ipt;
            answer += ipt;
        }
        cout << answer << endl;
    }
}
 