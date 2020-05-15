#include <ios>
#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int tc, b;
    long long int n, k, tmin, tmax, sum, mxset;
    cin >> tc;
    while (tc--) {
        cin >> n >> k >> b;
        tmin = 0;
        tmax = 0;
        for (int i = 0; i < b; i++)
            tmin += i+1;
        for (int i = 0; i < b; i++) {
            tmax += k-i;
            if (tmax >= n) break;
        }
        if (tmin <= n && n <= tmax) {
            sum = b*(long long int)(b+1)/2;
            mxset = 0;
            for (int i = b; i >= 1; i--) {
                if (sum-i+(k-mxset) >= n) {
                    std::cout << n-sum+i;
                    for (long long int j = 1; j < b-mxset; j++) cout << ' ' << j;
                    for (long long int j = k-mxset; j < k; j++) cout << ' ' << j+1;
                    cout << '\n';
                    break;
                } else {
                    sum -= i;
                    sum += (k-mxset);
                    mxset++;
                }
            }
        }
        else cout << -1 << '\n';
    }
}