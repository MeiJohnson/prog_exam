 
class Post():
  """
  Функция создания поста в гостевой книге

  (с) Царулкова Анастасия 2 группа 2020
  """
  def __init__(self,nick='Nick',text='Hello world!'): # Инициализация экземпляра класса
    self.__verify_text(nick) # Проверка псевдонима
    self.__verify_text(text) # Проверка текста
    self.__user_nick = nick  # Присвоение значения свойству экземпляра
    self.__user_text = text  # Присвоение значения свойству экземпляра
    
    """Ник"""
  @property
  def nickname(self):
    return self.__user_nick # getter
    
  @nickname.setter
  def nickname(self, nick): #setter
    try:
      self.__verify_text(nick)
    except ValueError as e:
      print(e)
    else:
      self.__user_nick = nick 

    """Текст записи"""
  @property
  def textPost(self):
    return self.__user_text
    
  @textPost.setter
  def textPost(self, text):
    try:
      self.__verify_text(text)
    except ValueError as e:
      print(e)
    else:
      self.__user_text = text 


  def __verify_text(self, text,field='text'):
    if len(text) == 0:
      raise ValueError(f'Поле {field} обязательное поле')

  def __str__(self): #Вывод содержания экземпляра
    return f"Author:{self.nickname} Text:{self.textPost}" 

class Comment(Post): # Наследует класс Post 
  """
  Функция создания комментария под постом в гостевой книге

  (с) Царулкова Анастасия 2 группа 2020
  """
  def __init__(self,nick, text, rate=0): 
    Post.__init__(self, nick, text) # вызов инициализатора класса, от которого наследует Comment
    self.__rate = rate

  @property
  def comRate(self):
    return self.__rate
  
  @comRate.setter
  def comRate(self,rate):
    self.__rate = rate

  def addRate(self): #Метод класса, который увеличивает рейтинг
    self.__rate += 1
  
  def __str__(self): #Вывод содержания экземпляра
    return f"Author:{self.nickname} Text:{self.textPost} Rating:{self.__rate}" 

re = Post('TwilightSparkle','Dear princess Celestia...')
print(re.nickname)
print(re.textPost)
print(re)
n = Comment('Nana','Hi everyone!')
print(n.nickname)
n.addRate()
#print(n.getRate())
print(n)
n.addRate()
print(n.comRate)
