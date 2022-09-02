import math
from line_log import get_logger

lg = get_logger(name="(line Comparsion_Finding Length)", file_name="line_log")


class LineComparison:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def calculate_length(self):
        """
        finding the length of two cartesian co-ordinates
        :return:None
        """
        try:
            length_xy = math.sqrt(math.pow(self.x2 - self.x1, 2) + math.pow(self.y2 - self.y1, 2))
            lg.debug(f'Length of value is: {length_xy}')
        except Exception as e:
            lg.error(e)


if __name__ == '__main__':
    print("Enter X,Y Co_Ordinates of the Point 1: ")
    x1 = int(input("Enter the value of x1:\n"))
    y1 = int(input("Enter the value of y1:\n"))
    print("Enter X,Y Co_Ordinates of the Point 2: ")
    x2 = int(input("Enter the value of x2:\n"))
    y2 = int(input("Enter the value of y2:\n"))
    line_length = LineComparison(x1, x2, y1, y2)
    line_length.calculate_length()
