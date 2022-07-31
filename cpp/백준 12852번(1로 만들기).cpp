#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, div2, div3;
    cin >> n;

    int dp[n+1] = {};

    for (int i = 2; i <= n; i++) {
        div2 = n;
        div3 = n;
        if (i % 2 == 0) {
            div2 = dp[i / 2];
        }
        if (i % 3 == 0) {
            div3 = dp[i / 3];
        }
        dp[i] = min({dp[i-1], div2, div3}) + 1;
    }

    cout << dp[n] << endl;
}

