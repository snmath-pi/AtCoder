#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define fi first
#define se second
map<ll, ld> mp;
ld dfs(ll n, ll a, ll x, ll y)
{
    
    if (mp.find(n) != mp.end())
        return mp[n];
    if (!n)
        return 0ll;
    ld &ans=mp[n];
    ld a1 = dfs(n/a,a,x,y)+x;
    ld b1 = 0;
    for (int i = 2; i <= 6; i++)
    {

        b1+= dfs(int64_t(n/i), a, x, y)/6;

    }
    b1 = (b1+y)*6/5;
    ans = min(a1, b1);
    return ans;
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll n, a, x, y;
    cin >> n >> a >> x >> y;
    cout << setprecision(6) << fixed;

    cout << dfs(n, a, x, y);
}