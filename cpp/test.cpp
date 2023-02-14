#include <iostream>
#include <string>
using namespace std;

int main()
{
  int t, l, e, e1, x, carry;
  string ipt, endString, answer;
  cin >> t;

  for (int zzz = 0; zzz < t; zzz++)
  {
    cin >> ipt;
    answer = "";
    carry = 0;
    while (ipt.length() > 1)
    {

      l = ipt.length();
      e = ipt.at(l - 1) - '0';
      cout << "e : " << e << endl;
      answer = to_string(e) + answer;
      ipt = ipt.substr(0, l - 1);
      x = 1;
      l = ipt.length();

      e1 = ipt.at(l - 1) - '0';
      if (e1 + carry >= e)
      {
        ipt = ipt.substr(0, l - x) + to_string(e1 - e + carry);
        carry = 0;
      }
      else
      {
        ipt = ipt.substr(0, l - x) + to_string(10 + e1 - e + carry);
        carry = -1;
      }
    }
    if (ipt.at(0) == '0')
    {
      if (answer.at(0) == '0')
        cout << answer.substr(1) << endl;
      else
      {
        cout << answer << endl;
      }
    }
    else
    {
      cout << 0 << endl;
    }
  }
}
