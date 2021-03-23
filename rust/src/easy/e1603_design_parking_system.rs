struct ParkingSystem {
    big: i32,
    medium: i32,
    small: i32,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ParkingSystem {
    fn new(big: i32, medium: i32, small: i32) -> Self {
        ParkingSystem { big, medium, small }
    }

    fn add_car(&mut self, car_type: i32) -> bool {
        match car_type {
            1 => {
                if self.big <= 0 {
                    return false;
                } else {
                    self.big -= 1;
                    return true;
                }
            }
            2 => {
                if self.medium <= 0 {
                    return false;
                } else {
                    self.medium -= 1;
                    return true;
                }
            }
            _ => {
                if self.small <= 0 {
                    return false;
                } else {
                    self.small -= 1;
                    return true;
                }
            }
        }
        true
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj = ParkingSystem::new(big, medium, small);
 * let ret_1: bool = obj.add_car(carType);
 */
#[test]
fn add_car() {
    let mut ps = ParkingSystem::new(1, 1, 0);
    assert_eq!(true, ps.add_car(1));
    assert_eq!(true, ps.add_car(2));
    assert_eq!(false, ps.add_car(3));
    assert_eq!(false, ps.add_car(1));
}
