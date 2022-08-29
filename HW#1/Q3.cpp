#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int k;
    long long x=1;
    cin>>k;
    
    queue<long>q3,q5,q7;
    for(int i=1;i<k;i++)
    {
        q3.push(x*3);
        q5.push(x*5);
        q7.push(x*7);
        x=min(min(q3.front(),q5.front()),q7.front());
        if(x==q3.front())
        {
            q3.pop();
        }
        if(x==q5.front())
        {
            q5.pop();
        }
        if(x==q7.front())
        {
            q7.pop();
        }
    }
    cout<<x<<"\n";
    return 0;
}