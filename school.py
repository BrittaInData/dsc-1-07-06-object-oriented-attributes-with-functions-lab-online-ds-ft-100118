# import copy for the last function
import copy

class School():
    
    def __init__(self, name):
        self.name = name  
        self._roster = {}
            
    def roster(self):
        return self._roster
        
    def grade(self, grade):
        return self._roster[grade]
        
    def add_student(self, name, grade):
        if grade in self._roster:
            self._roster[grade].append(name)
        else:
            self._roster[grade] = [name]
        return self._roster      
    
    def grade(self, grade):
        return self._roster[grade]    
    
    def sort_roster(self):
        sorted_dict = copy.deepcopy(self._roster)
        for key in sorted_dict:
            sorted_dict[key].sort()
        return sorted_dict