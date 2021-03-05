struct Solution;

impl Solution {
    pub fn count_matches(items: Vec<Vec<String>>, rule_key: String, rule_value: String) -> i32 {
        let index = match rule_key.as_str() {
            "type" => 0,
            "color" => 1,
            "name" => 2,
            &_ => 3,
        };

        let mut res = 0;
        for item in items {
            if item[index] == rule_value {
                res += 1;
            }
        }
        res
    }
}

#[test]
fn test_count_matches_1() {
    let items = vec![
        vec!["phone".to_string(), "blue".to_string(), "pixel".to_string()],
        vec![
            "computer".to_string(),
            "silver".to_string(),
            "lenovo".to_string(),
        ],
        vec![
            "phone".to_string(),
            "gold".to_string(),
            "iphone".to_string(),
        ],
    ];
    let rule_key = "color";
    let rule_value = "silver";
    assert_eq!(
        1,
        Solution::count_matches(items, rule_key.to_string(), rule_value.to_string())
    );
}

#[test]
fn test_count_matches_2() {
    let items = vec![
        vec!["phone".to_string(), "blue".to_string(), "pixel".to_string()],
        vec![
            "computer".to_string(),
            "silver".to_string(),
            "phone".to_string(),
        ],
        vec![
            "phone".to_string(),
            "gold".to_string(),
            "iphone".to_string(),
        ],
    ];
    let rule_key = "type";
    let rule_value = "phone";
    assert_eq!(
        2,
        Solution::count_matches(items, rule_key.to_string(), rule_value.to_string())
    );
}
