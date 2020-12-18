function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    let ans:number[] = [];

   let len = Math.floor((nums1.length+nums2.length)/2);
   let c = (nums1.length+nums2.length)%2;
   let i = 0,j = 0;
   while(true){
       if(nums1[i]!==undefined&&nums2[j]!==undefined){
            if(nums1[i]<nums2[j]){
            ans.push(nums1[i]);
            i++;
            };
            if(nums1[i]>nums2[j]) 
            {
                ans.push(nums2[j]);
                j++;
            }
            if(nums1[i]==nums2[j]) {
                ans.push(nums1[i]);
                //ans.push(nums2[j]);
                i++;
                //j++;
            };
       }
       else if(nums1[i]===undefined){
           ans.push(nums2[j]);
           j++;
       }
       else{
           ans.push(nums1[i]);
           i++;
       };
       console.log(ans);
       if(ans.length==len+1){
            if(c==0) return (ans[len-1]+ans[len])/2;
            else return ans[len];
       }
   };
};