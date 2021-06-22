
"""
Разработать программу для считывания данных JSON-формата из файла и вывод их в табличном виде на экран.
Организовать тестирование работоспособности программы с помощью assert, print.
"""

import json

def json_table(data):

  table = []
  sstr = '| {id:^3} | {first_name:^10} | {last_name:^15} | {email:^30} | {gender:^6} | {ip_address:^16} |'
  t_caption = '| {:^3} | {:^10} | {:^15} | {:^30} | {:^6} | {:^16} |'.format('id','first_name','last_name','email','gender','ip_address')
  roof = '-'*len(t_caption)
  
  table.append(roof)  
  table.append(t_caption)
  table.append(roof)  

  for el in range(len(data)):
      temp = data[el]
      res = sstr.format(**temp)
      table.append(res)
  table.append(roof)
  return(table)


import unittest

class TestFunc(unittest.TestCase):
  def setUp(self):
      with open('/home/vasya/Документы/Github/prog3/srTest/vsr/MOCKDATA.json') as f:
          data_dict = json.load(f)
      self.data = data_dict
  
  def test_equal(self):
      self.assertEqual(json_table(self.data)[1],'| id  | first_name |    last_name    |             email              | gender |    ip_address    |')

  def test_istuple(self):
      self.assertIs(type(json_table(self.data)),list)
  def test_in(self):
      self.assertIn(json_table(self.data)[1], 'familyname')      

if __name__ == '__main__':
    unittest.main()
