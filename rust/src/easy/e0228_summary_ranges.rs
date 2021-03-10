struct Solution;

impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        if nums.len() == 0 {
            return Vec::<String>::new();
        }
        let mut res: Vec<String> = vec![];
        let mut stack: Vec<i32> = vec![];
        for num in nums {
            if stack.len() == 0 {
                stack.push(num);
            } else {
                let mut last = stack[stack.len() - 1];
                if last != num - 1 {
                    res.push(Solution::ranges_value(&stack));
                    stack.clear();
                }
                stack.push(num);
            }
        }
        res.push(Solution::ranges_value(&stack));
        res
    }

    pub fn ranges_value(nums: &Vec<i32>) -> String {
        if nums.len() < 1 {
            "".to_string()
        } else if nums.len() == 1 {
            format!("{}", nums[0])
        } else {
            format!("{}->{}", nums[0], nums[nums.len() - 1])
        }
    }
}

#[test]
fn test_summary_ranges() {
    assert_eq!(
        vec!["0->2", "4->5", "7"],
        Solution::summary_ranges(vec![0, 1, 2, 4, 5, 7])
    );
    assert_eq!(
        vec!["0", "2->4", "6", "8->9"],
        Solution::summary_ranges(vec![0, 2, 3, 4, 6, 8, 9])
    );
    assert_eq!(Vec::<String>::new(), Solution::summary_ranges(vec![]));
    assert_eq!(vec!["-1"], Solution::summary_ranges(vec![-1]));
    assert_eq!(vec!["0"], Solution::summary_ranges(vec![0]));
}
