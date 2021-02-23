struct Solution;

impl Solution {
    fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        if nums.len() == 0 {
            return 0;
        }
        let mut i = 0;
        for j in 0..nums.len() {
            if nums[j] != val {
                nums[i] = nums[j];
                i = i + 1;
            }
        }
        i as i32
    }
}

#[test]
pub fn test_remove_element() {
    let mut v = vec![4, 5];
    assert_eq!(1, Solution::remove_element(&mut v, 4));
    assert_eq!(vec![5], &v[0..1]);

    let mut v = vec![3, 2, 2, 3];
    assert_eq!(2, Solution::remove_element(&mut v, 3));
    assert_eq!(vec![2, 2], &v[0..2]);

    let mut v = vec![0, 1, 2, 2, 3, 0, 4, 2];
    assert_eq!(5, Solution::remove_element(&mut v, 2));
    assert_eq!(vec![0, 1, 3, 0, 4], &v[0..5]);
}
