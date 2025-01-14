import unittest
from connected_cities import ConnectedCities

class TestConnectedCities(unittest.TestCase):
    def setUp(self):
        # Create a temporary test file with city connections
        self.test_file = "test_cities.txt"
        with open(self.test_file, 'w') as file:
            file.write("Bengaluru, Hyderabad\n")
            file.write("Chennai, Bengaluru\n")
            file.write("Hyderabad, Nagpur\n")
            file.write("Hyderabad, Vijayawada\n")
            file.write("Bengaluru, Kochi\n")
        
        self.cc = ConnectedCities(self.test_file)

    def tearDown(self):
        import os
        os.remove(self.test_file)

    def test_direct_connection(self):
        self.assertTrue(self.cc.are_connected("Bengaluru", "Hyderabad"))

    def test_indirect_connection(self):
        self.assertTrue(self.cc.are_connected("Chennai", "Nagpur"))

    def test_no_connection(self):
        self.assertFalse(self.cc.are_connected("Chennai", "Vijayawada"))

    def test_nonexistent_city(self):
        self.assertFalse(self.cc.are_connected("Mumbai", "Delhi"))

if __name__ == "__main__":
    unittest.main()