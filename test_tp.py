import unittest
from tp import *
class Test_tp(unittest.TestCase):
    def test_bubble_sort(self):
        sort_by = 0
        list = [("2","Amrit","Pangeni","Eth Hacking","Nawalparasi","9847095399"),
                    ("1","Anjal","Giri","B.Computing","Kathmandu","9847095398"),
                    ("3","David","Joshi","B.Commerce","Dhangadi","9847095397")]
        ex_result=[("1","Anjal","Giri","B.Computing","Kathmandu","9847095398"),
                   ("2", "Amrit", "Pangeni", "Eth Hacking", "Nawalparasi", "9847095399"),
                   ("3", "David", "Joshi", "B.Commerce", "Dhangadi", "9847095397")]
        ac_result=Softwarica.bubble_sort(list,sort_by)
        self.assertEqual(ex_result,ac_result)

    def test_search(self):
            search_by = 1  # searching by First Name, Change values accordance to index value to searching by different parameters.
            search_for = "Amrit"
            array_test =[("2","Anjal","Giri","Eth Hacking","Kalanki","9841554486"),
                    ("1","binod","Giri","B.Computing","Kathmandu","9847095398"),
                    ("3","suraj","J","B.Commerce","Dhangadi","9847095397")]

            expected_result = [("2","Anjal","Giri","Eth Hacking","Kalanki","9841554486")]
            mylist = Softwarica.search(array_test,search_by ,search_for)
            self.assertEqual(mylist, expected_result)



