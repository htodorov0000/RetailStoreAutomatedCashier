import unittest
from unittest import TestCase
from collection_of_goods import randomize_aisle_positions, start_pos
from product import aisles

class TestUniqueRandomizedPositions(TestCase):
    
    def test_randomize_aisle_positions(self):
        #test ran multiple times to ensure no duplicate positions can happen
        for i in range(0,100000):
            randomize_aisle_positions()
            for aisle in aisles:
                other_aisles = aisles.copy()
                other_aisles.remove(aisle)
                for other_aisle in other_aisles:
                    self.assertNotEqual(aisle.position, other_aisle.position)
                self.assertNotEqual(aisle.position, start_pos)

if __name__ == "__main__":
    unittest.main()