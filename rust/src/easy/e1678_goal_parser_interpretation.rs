struct Solution;

impl Solution {
    pub fn interpret(command: String) -> String {
        let mut n = 0;
        let mut res = String::from("");
        for c in command.chars() {
            if c == 'G' {
                res.push('G');
                continue;
            }
            if c == ')' {
                if n == 1 {
                    res.push('o');
                }
                if n == 3 {
                    res.push_str("al");
                }
                n = 0;
                continue;
            }
            n += 1;
        }
        res
    }
}

#[test]
pub fn test_interpret() {
    assert_eq!("Goal", Solution::interpret("G()(al)".to_string()));
    assert_eq!("Gooooal", Solution::interpret("G()()()()(al)".to_string()));
    assert_eq!(
        "alGalooG",
        Solution::interpret("(al)G(al)()()G".to_string())
    );
}
