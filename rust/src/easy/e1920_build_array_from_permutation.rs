struct Solution;

impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut res = vec![0; nums.len()];
        for i in 0..res.len() {
            res[i] = nums[nums[i] as usize]
        }
        res
    }
}

#[test]
fn test_build_array() {
    assert_eq!(vec![0,1,2,4,5,3], Solution::build_array(vec![0,2,1,5,3,4]));
    assert_eq!(vec![4,5,0,1,2,3], Solution::build_array(vec![5,0,1,2,3,4]));
}
