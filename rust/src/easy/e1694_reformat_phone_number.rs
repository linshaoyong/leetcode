struct Solution;

impl Solution {
    pub fn reformat_number(number: String) -> String {
        let mut res = vec![];
        let mut i = 0;
        for c in number.chars() {
            if c != ' ' && c != '-' {
                if i % 3 == 0 && i > 0 {
                    res.push('-');
                }
                res.push(c);
                i += 1;
            }
        }
        let length = res.len();
        if length > 4 && res[length - 2] == '-' && res[length - 5] != '-' {
            res[length - 2] = res[length - 3];
            res[length - 3] = '-';
        }
        res.iter().collect()
    }
}

#[test]
fn test_reformat_number() {
    assert_eq!(
        "123-456",
        Solution::reformat_number("1-23-45 6".to_string())
    );
    assert_eq!(
        "123-45-67",
        Solution::reformat_number("123 4-567".to_string())
    );
    assert_eq!(
        "123-456-78",
        Solution::reformat_number("123 4-5678".to_string())
    );
    assert_eq!("12", Solution::reformat_number("12".to_string()));
    assert_eq!(
        "175-229-353-94-75",
        Solution::reformat_number("--17-5 229 35-39475 ".to_string())
    );
}
