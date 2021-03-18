struct Solution;

impl Solution {
    pub fn special_array(nums: Vec<i32>) -> i32 {
        let mut count = nums.len() as i32;
        let mut sns = nums.clone();
        sns.sort();
        for (i, v) in sns.iter().enumerate() {
            if v >= &count {
                if i == 0 {
                    return count;
                }
                if sns[i - 1] < count {
                    return count;
                } else {
                    return -1;
                }
            }
            count -= 1;
        }
        -1
    }
}

#[test]
fn test_special_array() {
    assert_eq!(2, Solution::special_array(vec![3, 5]));
    assert_eq!(-1, Solution::special_array(vec![0, 0]));
    assert_eq!(3, Solution::special_array(vec![0, 4, 3, 0, 4]));
    assert_eq!(-1, Solution::special_array(vec![3, 6, 7, 7, 0]));
}
