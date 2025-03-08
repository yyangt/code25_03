#include<iostream>
#include<cmath>
class Vector3{
public:
  float x,y,z;
  Vector3(float x=0,float y=0,float z=0) :x(x),y(y),z(z){}
  Vector3 operator+(const Vector3& other )const{
    return Vector3(x+other.x,y+other.y,z+other.z);
  }
  Vector3 operator-(const Vector3& other )const{
    return Vector3(x-other.x,y-other.y,z-other.z);
  }
  Vector3 operator*(const float s )const{
    return Vector3(x*s,y*s,z*s);
  }
  float Dot(const Vector3& other) const {
    return x * other.x + y * other.y + z * other.z;
}
  Vector3 Cross(const Vector3& other) const {
    return Vector3(
        y * other.z - z * other.y,
        z * other.x - x * other.z,
        x * other.y - y * other.x
    );
  }
  Vector3 Normalize() const {
    float length = std::sqrt(x * x + y * y + z * z);
    if (length == 0) return *this;
    return *this * (1.0f / length);
}
};
int main()
{

}