struct Solution;

impl Solution {
    pub fn reorder_spaces(text: String) -> String {
        let mut spaces = 0;
        let mut words: Vec<String> = vec![];
        let mut word: Vec<char> = vec![];
        for c in text.chars() {
            if c == ' ' {
                spaces += 1;
                if word.len() > 0 {
                    words.push(word.iter().collect());
                    word.clear();
                }
            } else {
                word.push(c);
            }
        }
        if word.len() > 0 {
            words.push(word.iter().collect());
        }
        if words.len() == 1 {
            let mut res = words[0].clone();
            res.push_str(&" ".repeat(spaces));
            return res;
        }

        let sp = spaces / (words.len() - 1);
        let extra = spaces % (words.len() - 1);
        let mut words = words.join(&" ".repeat(sp));
        words.push_str(&" ".repeat(extra));
        words
    }
}

#[test]
fn test_reorder_spaces() {
    assert_eq!(
        "this   is   a   sentence",
        Solution::reorder_spaces("  this   is  a sentence ".to_string())
    );
    assert_eq!(
        "practice   makes   perfect ",
        Solution::reorder_spaces(" practice   makes   perfect".to_string())
    );
    assert_eq!(
        "hello   world",
        Solution::reorder_spaces("hello   world".to_string())
    );
    assert_eq!(
        "walks  udp  package  into  bar  a ",
        Solution::reorder_spaces("  walks  udp package   into  bar a".to_string())
    );
    assert_eq!("a", Solution::reorder_spaces("a".to_string()));
    assert_eq!("hello  ", Solution::reorder_spaces("  hello".to_string()));
}
