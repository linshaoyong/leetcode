struct Solution;

impl Solution {
    pub fn maximum_time(time: String) -> String {
        let mut cs: Vec<char> = time.chars().collect();
        let mut res: Vec<char> = vec![];

        let first = cs[0];
        match first {
            '?' => res.push(
                if cs[1] == '?' || cs[1] == '0' || cs[1] == '1' || cs[1] == '2' || cs[1] == '3' {
                    '2'
                } else {
                    '1'
                },
            ),
            x => res.push(x),
        }

        let second = cs[1];
        match second {
            '?' => res.push(if res[0] == '2' { '3' } else { '9' }),
            x => res.push(x),
        }

        res.push(':');

        let third = cs[3];
        match third {
            '?' => res.push('5'),
            x => res.push(x),
        }

        let forth = cs[4];
        match forth {
            '?' => res.push('9'),
            x => res.push(x),
        }

        res.iter().collect()
    }
}

#[test]
fn test_maximum_time() {
    assert_eq!("23:50", Solution::maximum_time("2?:?0".to_string()));
    assert_eq!("09:39", Solution::maximum_time("0?:3?".to_string()));
    assert_eq!("19:22", Solution::maximum_time("1?:22".to_string()));
    assert_eq!("14:03", Solution::maximum_time("?4:03".to_string()));
    assert_eq!("20:15", Solution::maximum_time("?0:15".to_string()));
}
