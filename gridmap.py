from typing import Callable


class GridPlan:
    separator = ','
    single_char = False
    fill_gaps = False
    default_value = 0
    text = ""
    size_x = 0
    size_y = 0


class GridMap:
    grid = None

    def __init__(self, size_x=100, size_y=100, grid_value=0, grid_plan=None):
        if not (grid_plan is None):
            self.grid = self.gen_grid(size_x, size_y, grid_value)
        else:
            self.grid = self.gen_grid(size_x, size_y, grid_value)

    @staticmethod
    def gen_grid(size_x, size_y, value=0):
        """Create grid of size X,Y populated with default value provided"""
        return [[value for _ in range(size_y)] for _ in range(size_x)]

    @staticmethod
    def gen_grid_from_plan(self, plan: GridPlan):
        """Create grid from GridPlan object"""
        pass

    @staticmethod
    def get_top_left_point_of_range(pos_x_1, pos_y_1, pos_x_2, pos_y_2):
        x = min(pos_x_1, pos_x_2)
        y = min(pos_y_1, pos_y_2)
        return [x, y]

    @staticmethod
    def get_bottom_right_point_of_range(pos_x_1, pos_y_1, pos_x_2, pos_y_2):
        x = max(pos_x_1, pos_x_2)
        y = max(pos_y_1, pos_y_2)
        return [x, y]

    def get_length_x(self):
        """Get grid Y length"""
        return len(self.grid)

    def get_length_y(self):
        """Get grid Y length"""
        return len(self.grid[0])

    def set_grid_point(self, pos_x, pos_y, value):
        """Set grid value at point X,Y"""
        self.grid[pos_x][pos_y] = value
        return self.grid[pos_x][pos_y]

    def get_grid_point(self, pos_x, pos_y):
        """Get grid value at point X,Y"""
        return self.grid[pos_x][pos_y]

    def _for_point_in_grid_selection(self, pos_x_1: int, pos_y_1: int, pos_x_2: int, pos_y_2: int, callback: Callable,
                                     write_to_grid=False):
        """Helper function. Runs callback for each point in specified sub-grid. Defaults to readonly but can be set
        to write to grid when write_to_grid=True. Returns resulting sub-grid

        pos 1 x & y must be <= pos 2 x & y"""

        # Guard for pos 1 > pos 2
        if (not self.point_is_in_grid(pos_x_1, pos_y_1)) or (not self.point_is_in_grid(pos_x_2, pos_y_2)):
            raise IndexError("Specified point outside grid.")

        new_sub_grid = []
        for x in range(pos_x_1, pos_x_2 + 1):
            new_sub_grid.append([])
            for y in range(pos_y_1, pos_y_2 + 1):
                result = callback(pos_x=x, pos_y=y)
                new_sub_grid[x].append(result)
                if write_to_grid:
                    old_grid_x = pos_x_1 + x
                    old_grid_y = pos_y_1 + y
                    self.set_grid_point(old_grid_x, old_grid_y, result)
        return new_sub_grid

    def set_grid_rect(self, pos_x_1, pos_y_1, pos_x_2, pos_y_2, value):
        # Create curried function for _for_point_in_grid_selection callback
        def set_grid_point_value(value):
            def set_grid_point_pos(pos_x, pos_y):
                return value
            return set_grid_point_pos

        # Curry value
        callback = set_grid_point_value(value)
        # Execute grid transform
        return self._for_point_in_grid_selection(pos_x_1, pos_y_1, pos_x_2, pos_y_2, callback, write_to_grid=True)

    def get_grid_rect(self, pos_x_1, pos_y_1, pos_x_2, pos_y_2):
        return self._for_point_in_grid_selection(pos_x_1, pos_y_1, pos_x_2, pos_y_2, self.get_grid_point)

    def point_is_in_grid(self, pos_x, pos_y):
        """Returns True if specified point is within grid"""
        return 0 <= pos_x < self.get_length_x() and 0 <= pos_y < self.get_length_y()




