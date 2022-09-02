import math
from line_log import get_logger

lg = get_logger(name="(line Comparsion_Finding Length)", file_name="line_log")


class LineComparison:
    def __init__(self, line_dict):
        self.x1 = line_dict.get("x1")
        self.x2 = line_dict.get("x2")
        self.y1 = line_dict.get("y1")
        self.y2 = line_dict.get("y2")

    def calculate_length(self):
        """
        finding the length of two cartesian co-ordinates
        :return:None
        """
        try:
            length_xy = math.sqrt(math.pow(self.x2 - self.x1, 2) + math.pow(self.y2 - self.y1, 2))
            lg.debug(f'Length of value is: {length_xy}')
            return length_xy
        except Exception as e:
            lg.error(e)


if __name__ == '__main__':
    def add_line():
        """
        inserting values to the x and y co-ordinates
        :return: object of line comparison class
        """
        try:
            print("Enter X,Y Co_Ordinates of the Point 1: ")
            x1 = int(input("Enter the value of x1:\n"))
            y1 = int(input("Enter the value of y1:\n"))
            print("Enter X,Y Co_Ordinates of the Point 2: ")
            x2 = int(input("Enter the value of x2:\n"))
            y2 = int(input("Enter the value of y2:\n"))
            line_dict = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
            line_obj = LineComparison(line_dict)
            return line_obj
        except Exception as e:
            lg.error(e)

    print("Enter X,Y Co_Ordinates of the line 1:\n")
    line_one = add_line().calculate_length()
    lg.info(line_one)
    print("Enter X,Y Co_Ordinates of the line 2:\n")
    line_two = add_line().calculate_length()
    lg.info(line_two)

    lg.debug("Both line length are equal" if line_one == line_two else
          "Both line length are not equal")



