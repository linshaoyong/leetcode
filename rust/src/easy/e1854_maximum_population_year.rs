use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn maximum_population(logs: Vec<Vec<i32>>) -> i32 {
        let mut map = HashMap::<i32, i32>::new();
        for log in &logs {
            for year in log[0]..log[1] {
                *map.entry(year).or_insert(0) += 1;
            }
        }

        let mut max_population = 0;
        let mut min_year = logs[0][0];
        for (year, population) in map.iter() {
            if population > &max_population {
                max_population = *population;
                min_year = *year;
            }
            if population == &max_population {
                if year < &min_year {
                    min_year = *year;
                }
            }
        }
        min_year
    }
}

#[test]
fn test_maximum_population() {
    assert_eq!(
        1993,
        Solution::maximum_population(vec![vec![1993, 1999], vec![2000, 2010]])
    );
    assert_eq!(
        1960,
        Solution::maximum_population(vec![vec![1950, 1961], vec![1960, 1971], vec![1970, 1981]])
    );
}
