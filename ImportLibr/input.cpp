#include<iostream>
#include<algorithm>
// find(x,x + 2,4)
using namespace std;

int main(){
    int x[2];
    x[0] = 4;
    sort(x  x + 2);
    // fill(x,x + 2);
    // cout << "VALUE :"<< *find(x,x + 2,4);
    cout << x[1];
    return 0;
}