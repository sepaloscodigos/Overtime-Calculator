def read_file(filename):
    """
    reads in a file and adds each line from the file into a list with the "new line"
    (\n) characters taken off
    :param filename: the file that you want to read
    :return: a list where each element is a line from the file you passed in
    (with the \n character taken off)
    """
    file = open(filename)
    lines_in_file = file.readlines()
    # take off the \n from each line
    new_lines = []
    for line in lines_in_file:
        new_line = line.strip()
        new_lines.append(new_line)
    return new_lines

def calc_overtime_pay(new_lines):
    """
    using a list that has lines from a file as elements, 
    :param new_lines:
    :return:
    """
    for i in range(len(new_lines)):
        # if an employee is found, assign the employee's name, the amount of hours they have
        # worked, and their wage to a tuple. This will only work if the file is always formatted the same.
        if new_lines[i][:8] == "employee":
            employee = (new_lines[i][10:],
                        new_lines[i + 1][14:],
                        new_lines[i + 2][13:])
            name, hours_worked, wage = employee
            int_hours_worked = int(hours_worked)
            int_wage = int(wage)
            # if they have worked more than 40 hours, calculate their overtime pay.
            if int_hours_worked > 40:
                overtime_hours = int_hours_worked - 40
                overtime_pay = int_wage * 1.5 * overtime_hours
                print(name, "has earned", overtime_pay, "dollars in overtime pay.")
            else:
                print(name, "has not earned overtime pay.")

def main():
    """
    calls the functions to read the file and calculate any overtime pay earned
    :return: None
    """
    new_lines = read_file("hours_worked.txt")
    calc_overtime_pay(new_lines)

if __name__=="__main__":
    main()