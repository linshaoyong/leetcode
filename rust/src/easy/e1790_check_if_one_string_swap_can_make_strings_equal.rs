struct Solution;

impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        let sb1 = s1.as_bytes();
        let sb2 = s2.as_bytes();
        let mut indexs = vec![];
        for i in 0..sb1.len() {
            if sb1[i] != sb2[i] {
                indexs.push(i);
                if indexs.len() > 2 {
                    return false;
                }
            }
        }
        if indexs.len() == 0 {
            return true;
        }
        if indexs.len() == 2 {
            if sb2[indexs[0]] == sb1[indexs[1]] && sb2[indexs[1]] == sb1[indexs[0]] {
                return true;
            }
        }
        false
    }
}

#[test]
fn test_are_almost_equal() {
    assert!(Solution::are_almost_equal(
        "bank".to_string(),
        "kanb".to_string()
    ));
    assert!(Solution::are_almost_equal("attack".to_string(), "defend".to_string()) == false);
    assert!(Solution::are_almost_equal(
        "kelb".to_string(),
        "kelb".to_string()
    ));
    assert!(Solution::are_almost_equal("abce".to_string(), "dcba".to_string()) == false);
}
