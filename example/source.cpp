#include <iostream>
#include <vector>

using namespace std;

int main(){
    cout<<"Hello World!"<<endl;
    vector<int> v;
    int k=0;
    v.resize(200000000);
    for(int i=0; i<1000000000; i++){
        v[k%1000000]=k;
        k++;
    }
}