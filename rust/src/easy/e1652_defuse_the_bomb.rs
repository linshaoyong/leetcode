struct Solution;

impl Solution {
    pub fn decrypt(code: Vec<i32>, k: i32) -> Vec<i32> {
        let mut res = vec![0; code.len()];
        if k == 0 {
            return res;
        }

        let mut offset = 0;
        if k < 0 {
            offset = (code.len() as i32 + k - 1) as usize;
        }

        for i in 0..res.len() {
            let mut mk = k.abs() as usize;
            while mk > 0 {
                let j = (i + mk + offset) % code.len();
                res[i] += code[j];
                mk -= 1;
            }
        }
        res
    }
}

#[test]
fn test_decrypt() {
    assert_eq!(vec![12, 10, 16, 13], Solution::decrypt(vec![5, 7, 1, 4], 3));
    assert_eq!(vec![0, 0, 0, 0], Solution::decrypt(vec![1, 2, 3, 4], 0));
    assert_eq!(vec![12, 5, 6, 13], Solution::decrypt(vec![2, 4, 9, 3], -2));
}
