struct Solution;

impl Solution {
    pub fn count_asterisks(s: String) -> i32 {
        let mut res = 0;
        let mut current = 0;
        let mut count = 0;
        for c in s.chars() {
            if c == '*' {
                current += 1;
            }
            if c == '|' {
                count += 1;
                if count % 2 == 1 {
                    res += current;
                }
                current = 0;
            }
        }
        res + current
    }
}

#[test]
fn test_count_asterisks() {
    assert_eq!(2, Solution::count_asterisks("l|*e*et|c**o|*de|".to_string()));
    assert_eq!(0, Solution::count_asterisks("iamprogrammer".to_string()));
    assert_eq!(5, Solution::count_asterisks("yo|uar|e**|b|e***au|tifu|l".to_string()));
}