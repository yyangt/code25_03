#include<iostream>
#include<cmath>
using namespace std;

struct point {
  double x;
  double y;
  point(double x,double y) : x(x),y(y){}
};
double caculate(point p1,point p2)
{
  double dx=p2.x-p1.x;
  double dy=p2.y-p1.y;
  return sqrt(dx*dx+dy*dy);

}
int main()
{
  point p1(116.3,39.9),p2(121.4,31.2);
  double dis=caculate(p1,p2);
  cout<<"两点之间欧氏距离为:" <<dis<<endl;
  return 0;
}