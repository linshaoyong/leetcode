class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                nums.append('FizzBuzz')
                continue
            if i % 3 == 0:
                nums.append('Fizz')
                continue
            if i % 5 == 0:
                nums.append('Buzz')
                continue
            nums.append(str(i))
        return nums


def test_fizz_buzz():
    assert Solution().fizzBuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
    assert Solution().fizzBuzz(3) == ["1", "2", "Fizz"]
