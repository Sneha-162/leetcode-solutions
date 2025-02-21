class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int st = 1,end=arr.size()-2;    //optimazation bcz according to the Question leftmost start point and rightmost end point cannot be the peak points
        while(st<=end){
            int peak = st + (end-st)/2;

            if(arr[peak-1]<arr[peak] && arr[peak]>arr[peak+1]){
                return peak;
            }
            else if (arr[peak-1]<arr[peak]){
                st = peak+1;
            }
            else{
                end = peak-1;
            }
        }
        return -1;
        
    }
};
