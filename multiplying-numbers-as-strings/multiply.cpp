#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;

string multiply(string a, string b) {
    if (a == "0" || b == "0") return "0";
    
    vector<int> result(a.size() + b.size(), 0);
    
    for (auto i=a.size(); i-- > 0;)
        for (auto j=b.size(); j-- > 0;) {
            result[i+j+1] += (a[i]-'0') * (b[j]-'0');
            result[i+j] += result[i+j+1] / 10;
            result[i+j+1] %= 10;
        }
    
    string product;
    for (auto digit : result)
        if (!(product.empty() && digit == 0)) product += to_string(digit);
    
    return product;
}

int main() {
    assert(multiply("2", "3") == "6");
    assert(multiply("58608473622772837728372827", "7586374672263726736374") == \
        "444625839871840560024489175424316205566214109298");
    return 0;
}
