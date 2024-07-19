#include <iostream>
using namespace std;
int main() {
float popNJ = 9.27;
for (int i = 2021; i <= 2030; i++) {
cout << i << "\t" << popNJ << endl;
popNJ += popNJ*(12.0/1000) - popNJ*(7.8/1000);
}
return 0;
}