import win32com.client as win32
class Soldier:
    def __init__(self, _생활관, _이름, _계급):
        self.생활관 = _생활관
        self.이름 = _이름
        self.계급 = _계급

    def get_string_info(self):
        string_info = f'{self.계급} {self.이름}({self.생활관})'
        return string_info

# name = '박일규'
# info = {}
# info[name] = Soldier('군2',name,'상병')
# print(info[name].get_string_info())

class Excel:
    def __init__(self,filepath):
        self.excel = win32.Dispatch('Hcell.Application')
