class NewReg():
  """Класс для формы регистрации
    Анастасия Царулкова (с)"""

  attrDict = {}

  def __init__(self, fname, sname, email, affilation, u_year, u_country, u_city, u_pcode):
    self.__verify_text(fname, 'fname')
    self.__verify_text(sname, 'sname')
    self.__verify_email(email)
    self.__verify_text(affilation, 'affilation')
    self.__verify_year(u_year)
    self.__verify_text(u_country,'country')
    self.__verify_text(u_city,'city')
    self.__verify_pcode(u_pcode)
    self.__user_fname, self.__user_email, self.__user_sname, self.__user_affil, self.__user_year, self.__user_city, self.__user_country, self.__user_pcode = fname, sname, email, affilation, u_year, u_country, u_city, u_pcode
    
  def __getattr__(self, attr):
    return NewReg.attrDict.get(attr, 'No attribute or value')

  def __setattr__(self, attr, val):
        if (attr not in self.__dict__):
          NewReg.attrDict[attr] = val 

  """Имя"""
  @property
  def f_name(self):
    return self.__user_fname
    
  @f_name.setter
  def f_name(self, fname):
    try:
      self.__verify_text(fname,'fname')
    except ValueError as e:
      print(e)
    else:
      self.__user_fname = fname 

  """Фамилия"""
  @property
  def s_name(self):
    return self.__user_sname
    
  @s_name.setter
  def s_name(self, sname):
    try:
      self.__verify_text(sname,'sname')
    except ValueError as e:
      print(e)
    else:
      self.__user_sname = sname

  """Почта"""
  @property
  def e_mail(self):
    return self.__user_email
    
  @e_mail.setter
  def e_mail(self, email):
    try:
      self.__verify_email(email)
    except ValueError as e:
      print(e)
    else:
      self.__user_email = email
      
  """Образование"""
  @property
  def affil(self):
    return self.__user_affil
    
  @affil.setter
  def affil(self,affilation):
    try:
      self.__verify_text(affilation, 'affilation')
    except ValueError as e:
      print(e)
    else:
      self.__user_affil = affilation

  """Год рождения"""
  @property
  def year(self):
    return self.__user_year
    
  @year.setter
  def year(self, u_year):
    try:
      self.__verify_year(u_year)
    except ValueError as e:
      print(e)
    else:
      self.__user_year = u_year

  """Страна"""
  @property
  def country(self):
    return self.__user_country 
    
  @country.setter
  def country(self, u_country):
    try:
      self.__verify_text(u_country,'country')
    except ValueError as e:
      print(e)
    else:
      self.__user_country = u_country 

  """Город"""
  @property
  def city(self):
    return self.__user_city
    
  @city.setter
  def city(self, u_city):
    try:
      self.__verify_text(u_city,'city')
    except ValueError as e:
      print(e)
    else:
      self.__user_city = u_city 
    
  """Почтовый индекс"""
  @property
  def pcode(self):
    return self.__user_pcode
    
  @pcode.setter
  def pcode(self, u_pcode):
    try:
      self.__verify_pcode(u_pcode)
    except ValueError as e:
      print(e)
    else:
      self.__user_pcode = u_pcode

          
        
  def __verify_text(self, text,field='text'):
    if len(text) == 0:
      raise ValueError(f'Поле {field} обязательное поле')
    if len(text) <= 1:
      raise ValueError(f'Поле {field} содержит меньше двух символов')
    if text.isdigit() == True:
      raise ValueError(f'Поле {field} содержит цифры')
    if text[0].isupper == False:
      raise ValueError(f'Поле {field} написано с маленькой буквы')
    
            
  def __verify_email(self, email):
    if len(email) == 0:
      raise ValueError('Поле Почта - обязательное поле') 
    if email.find('@') == -1:
      raise ValueError('Почта введена не корректно, нет символа @')
    temp = email.split('@')
    if temp[0] == '' or temp[1] == '':
      raise ValueError('Почта введена не корректно')

  
  def __verify_year(self, u_year):
    if len(u_year) == 0:
      raise ValueError('Это обязательное поле')
    if u_year.isdigit() == False:
      raise ValueError('Поле Год содержит недопустимые символы')
    if len(u_year) != 4:
      raise ValueError('Поле Год содержит недопустимое количество символов')
    
  
  def __verify_pcode(self, u_pcode):
    if len(u_pcode) != 6 or len(u_pcode) == 0:
      raise ValueError('Поле Почтовый индекс содержит недопустимое количество символов')
    if u_pcode.isdigit() == False:
      raise ValueError('Поле Почтовый индекс содержит недопустимые символы')
  


newform = NewReg('Ася','Васикова','lol@mail.ru','РГПУ','2025', 'Российская Федерация','Пенза','343485')
#print(newform._newform__user_sname)
print(newform.f_name)
newform.f_name = '77'
print(newform.f_name)
nf2 = NewReg('Ася','Васикова','lol@mail.ru','РГПУ','2025', 'Российская Федерация','Пенза','343485')
nf2.fname = 'Mama'
print(nf2.fname) 
