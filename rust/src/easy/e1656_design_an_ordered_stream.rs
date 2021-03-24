struct OrderedStream {
    values: Vec<String>,
    min_id: usize,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl OrderedStream {
    fn new(n: i32) -> Self {
        OrderedStream {
            values: vec!["".to_string(); n as usize + 1],
            min_id: 1,
        }
    }

    fn insert(&mut self, id_key: i32, value: String) -> Vec<String> {
        let mut m_id_key = id_key as usize;
        self.values[m_id_key] = value;
        let mut res = Vec::<String>::new();
        if self.min_id == m_id_key {
            while self.min_id < self.values.len() && self.values[self.min_id] != "" {
                res.push(self.values[self.min_id].clone());
                self.min_id += 1;
            }
        }
        res
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * let obj = OrderedStream::new(n);
 * let ret_1: Vec<String> = obj.insert(idKey, value);
 */
#[test]
fn test_insert() {
    let mut os = OrderedStream::new(5);
    assert_eq!(Vec::<String>::new(), os.insert(3, "ccccc".to_string()));
    assert_eq!(vec!["aaaaa"], os.insert(1, "aaaaa".to_string()));
    assert_eq!(vec!["bbbbb", "ccccc"], os.insert(2, "bbbbb".to_string()));
    assert_eq!(Vec::<String>::new(), os.insert(5, "eeeee".to_string()));
    assert_eq!(vec!["ddddd", "eeeee"], os.insert(4, "ddddd".to_string()));
}
