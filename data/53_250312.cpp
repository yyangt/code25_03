// 最大子数组和
#include<iostream>
#include<algorithm>
using namespace std;
int main(){
  int nums[10001];
  int n;
  cin>>n;
  for(int i=0;i<n;i++){
    cin>>nums[i];
  }        
  int sum;
  int ans=nums[0];
  for(int i=0;i<n;i++)
  {
      sum=sum+nums[i];
      if(sum<0)
      {
          sum=0;
      }
      ans=max(sum,ans);
  }
  cout<<ans;
  return 0;
}
  