#include<iostream>
using namespace std;
int func(int x){
    return x + 2;
}
int main(){
    int count = 4;
    cout << func(count,2);
}