# https://github.com/marvanekanayake/lab10-ME-AG-/
# Partner 1: Marvan Ekanayake
# Partner 2: Adrian Garced

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        assert(add(1, 1) == 2)
        assert(add(16, 4) == 20)
        assert(add(200, 300) == 500)

    def test_subtract(self): # 3 assertions
        assert(sub(1, 1) == 0)
        assert(sub(-16, 4) == -20)
        assert(sub(100, 50) == 50)
    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        assert(mul(1,1) == 1)
        assert(mul(1,2) == 2)
        assert(mul(2,1) == 2)


    def test_divide(self): # 3 assertions
        assert(div(1,1) == 1)
        assert(div(4,2) == 2)
        assert(div(2,1) == 2)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        assert(log(3, 9) == 2)
        assert(round(log(5, 125)) == 3) # round to avoid a floating point precision error
        assert(log(10, 10) == 1)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(0, 5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
         #call log function inside, example:
            with self.assertRaises(ValueError):
                log(0,5)


    def test_hypotenuse(self): # 3 assertions
        assert(hypotenuse(5, 12) == 13)
        assert(hypotenuse(3, 4) == 5)
        assert(hypotenuse(8, 6) == 10)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
            square_root(-10)
            square_root(-67)



# Do not touch this
if __name__ == "__main__":
    unittest.main()