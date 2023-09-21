'''
Author: yizhencode zhangyizhenyizen@gmail.com
Date: 2023-09-20 21:21:46
LastEditors: yizhencode zhangyizhenyizen@gmail.com
LastEditTime: 2023-09-20 21:33:04
FilePath: /6156_hw1/e6156-microservice-1/resources/students.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import json


class StudentsResource:
    #
    # This code is just to get us started.
    # It is also pretty sloppy code.
    #

    students_file = \
        "/Users/yizhenzhang/Desktop/6156_hw1/e6156-microservice-1/resources/old-students.json"

    def __init__(self):
        self.students = None

        with open(self.students_file, "r") as j_file:
            self.students = json.load(j_file)

    def get_students(self):
        return self.students
