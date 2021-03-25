use core::cmp::max;

struct Solution;

impl Solution {
    pub fn max_repeating(sequence: String, word: String) -> i32 {
        let mut res = 0;
        let step = word.len();
        for i in 0..step {
            let mut count = 0;
            for j in (i..sequence.len()).step_by(step) {
                if j + step > sequence.len() {
                    break;
                }
                if &sequence[j..j + step] == word {
                    count += 1;
                    res = max(res, count);
                } else {
                    count = 0;
                }
            }
        }
        res
    }
}

#[test]
fn test_max_repeating() {
    assert_eq!(
        2,
        Solution::max_repeating("ababc".to_string(), "ab".to_string())
    );
    assert_eq!(
        1,
        Solution::max_repeating("ababc".to_string(), "ba".to_string())
    );
    assert_eq!(
        0,
        Solution::max_repeating("ababc".to_string(), "ac".to_string())
    );
    assert_eq!(
        1,
        Solution::max_repeating("aaaaa".to_string(), "aaa".to_string())
    );
}
