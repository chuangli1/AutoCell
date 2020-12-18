function findMedianSortedArrays(nums1, nums2) {
    var ans = [];
    var len = Math.floor((nums1.length + nums2.length) / 2);
    var c = (nums1.length + nums2.length) % 2;
    var i = 0, j = 0;
    while (true) {
        console.log(nums1[i],nums2[j])
        if (nums1[i] !== undefined && nums2[j] !== undefined) {
            if (nums1[i] < nums2[j]) {
                ans.push(nums1[i]);
                i++;
            }
            if (nums1[i] > nums2[j]) {
                ans.push(nums2[j]);
                j++;
            }
            if (nums1[i] == nums2[j]) {
                ans.push(nums1[i]);
                //ans.push(nums2[j]);
                i++;
                //j++;
            }
            ;
        }
        else if (nums1[i] === undefined) {
            ans.push(nums2[j]);
            j++;
        }
        else {
            ans.push(nums1[i]);
            i++;
        }
        ;
        console.log(ans);
        if(ans.length>3) break;
        if (ans.length == len + 1) {
            if (c == 0)
                return (ans[len - 1] + ans[len]) / 2;
            else
                return ans[len];
        }
    }
    ;
};

findMedianSortedArrays([1,2,3,5],[4])
