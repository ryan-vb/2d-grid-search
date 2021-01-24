import unittest

import gridmap


class GridMapGenGrid(unittest.TestCase):
    def test_gridmap_grid_default(self):
        am = gridmap.GridMap(10, 10, 1)
        self.assertIsNotNone(am.grid)

    def test_gridmap_gen_grid_x(self):
        grid_square = gridmap.GridMap.gen_grid(10, 10)
        self.assertEqual(len(grid_square), 10)

    def test_gridmap_gen_grid_y(self):
        grid_square = gridmap.GridMap.gen_grid(10, 10)
        self.assertEqual(len(grid_square[0]), 10)
        self.assertEqual(len(grid_square[1]), 10)
        self.assertEqual(len(grid_square[2]), 10)
        self.assertEqual(len(grid_square[3]), 10)
        self.assertEqual(len(grid_square[4]), 10)
        self.assertEqual(len(grid_square[5]), 10)
        self.assertEqual(len(grid_square[6]), 10)
        self.assertEqual(len(grid_square[7]), 10)
        self.assertEqual(len(grid_square[8]), 10)
        self.assertEqual(len(grid_square[9]), 10)
        with self.assertRaises(IndexError):
            grid_square[10]

    def test_gridmap_gen_grid_value_str(self):
        grid_square = gridmap.GridMap.gen_grid(10, 10, "A")
        for col in grid_square:
            for point in col:
                self.assertEqual(point, "A")

    def test_gridmap_gen_grid_value_bool(self):
        grid_square = gridmap.GridMap.gen_grid(10, 10, True)
        for col in grid_square:
            for point in col:
                self.assertEqual(point, True)


# class GridMapGenGridFromString(unittest.TestCase):
#     def test_gridmap_grid_default(self):
#         """
#
#         """
#         am = gridmap.GridMap(10, 10, 1)
#         self.assertTrue(False)


class GridMapSingleGettersSetters(unittest.TestCase):
    def test_gridmap_get_top_left(self):
        pos_1 = 6, 9
        pos_2 = 4, 3
        tl_x, tl_y = gridmap.GridMap.get_top_left_point_of_range(*pos_1, *pos_2)
        self.assertEqual(4, tl_x)
        self.assertEqual(3, tl_y)

    def test_gridmap_get_top_left(self):
        pos_1 = 6, 9
        pos_2 = 4, 3
        br_x, br_y = gridmap.GridMap.get_bottom_right_point_of_range(*pos_1, *pos_2)
        self.assertEqual(6, br_x)
        self.assertEqual(9, br_y)

    def test_gridmap_get_length_x(self):
        am = gridmap.GridMap(12, 8)
        self.assertEqual(12, am.get_length_x())

    def test_gridmap_get_length_x(self):
        am = gridmap.GridMap(12, 8)
        self.assertEqual(12, am.get_length_x())

    def test_gridmap_get_length_y(self):
        am = gridmap.GridMap(12, 8)
        self.assertEqual(8, am.get_length_y())

    def test_gridmap_get_grid_point_0(self):
        am = gridmap.GridMap(12, 8, -1)
        self.assertEqual(-1, am.get_grid_point(0, 0))

    def test_gridmap_get_grid_point_1(self):
        am = gridmap.GridMap(12, 8, 1)
        self.assertEqual(1, am.get_grid_point(11, 7))

    def test_gridmap_get_grid_point_index_error_max_x(self):
        am = gridmap.GridMap(12, 8, 1)
        with self.assertRaises(IndexError):
            am.get_grid_point(12, 7)

    def test_gridmap_get_grid_point_index_error_max_y(self):
        am = gridmap.GridMap(12, 8, 1)
        with self.assertRaises(IndexError):
            am.get_grid_point(11, 8)

    def test_gridmap_set_grid_point(self):
        am = gridmap.GridMap(12, 8, -1)
        am.set_grid_point(8, 5, 0)
        self.assertEqual(0, am.get_grid_point(8, 5))

    def test_gridmap_set_grid_point(self):
        am = gridmap.GridMap(12, 8, -1)
        with self.assertRaises(IndexError):
            am.set_grid_point(12, 8, 0)

    def test_gridmap_get_grid_rect(self):
        am = gridmap.GridMap(12, 8, -1)
        sub_grid = am.get_grid_rect(0, 0, 11, 7)
        self.assertEqual(am.grid, sub_grid)

    @unittest.skip
    def test_gridmap_get_grid_rect_p2_lt_p1(self):
        am = gridmap.GridMap(12, 8, -1)
        sub_grid = am.get_grid_rect(11, 7, 0, 0)
        self.assertEqual(am.grid, sub_grid)

    def test_gridmap_set_grid_rect(self):
        am = gridmap.GridMap(4, 4, -1)
        sub_grid = am.set_grid_rect(0, 0, 3, 3, 1)
        expected = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(expected, sub_grid)
        self.assertEqual(am.grid, sub_grid)


if __name__ == '__main__':
    unittest.main()
