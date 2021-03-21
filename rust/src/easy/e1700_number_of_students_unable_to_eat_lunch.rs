struct Solution;

impl Solution {
    pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {
        let mut students = students.clone();
        let mut sandwiches = sandwiches.clone();
        let mut circulars = students.iter().filter(|&n| *n == 0).count();
        let mut squares = students.len() - circulars;
        while students.len() > 0 {
            if sandwiches[0] == 0 {
                if students[0] == 0 {
                    students.remove(0);
                    sandwiches.remove(0);
                    circulars -= 1;
                } else {
                    if circulars == 0 {
                        break;
                    }
                    students.remove(0);
                    students.push(1);
                }
            } else {
                if students[0] == 1 {
                    students.remove(0);
                    sandwiches.remove(0);
                    squares -= 1;
                } else {
                    if squares == 0 {
                        break;
                    }
                    students.remove(0);
                    students.push(0);
                }
            }
        }
        students.len() as i32
    }
}

#[test]
fn test_count_students() {
    assert_eq!(
        0,
        Solution::count_students(vec![1, 1, 0, 0], vec![0, 1, 0, 1])
    );
    assert_eq!(
        3,
        Solution::count_students(vec![1, 1, 1, 0, 0, 1], vec![1, 0, 0, 0, 1, 1])
    );
}
