import sys, re
from handlers import *
from util import *
from rules import *


class Parser:
    """
    Parser 读取文本文件，应用 规则并 控制处理程序
    """
   def _init_(self,handler):
       self.handler=handler