#include <iostream>
#include <limits>
using namespace std;

int main()
{

int n, k;
cin>>n>>k;
int arr[n];

for (int i = 0; i < n; ++i)
{
    cin >> arr[i];
}

for(int c = 0; c < k; c++){
 
    int max_so_far = numeric_limits<int>::min();
    int max_here = 0;

    int start = 0, end = 0, s = 0;
    for(int i = 0; i < n; i++)
    {
        max_here += arr[i];
        if (max_so_far < max_here)
        {
            max_so_far = max_here;
            start = s;
            end = i;
        }
        if (max_here < 0)
        {
            max_here = 0;
            s = i + 1;
        }
    }

    cout <<max_so_far<<endl;

    for (int l = start; l <= end; l++)
        arr[l] = numeric_limits<int>::min();
}

return 0;
}