#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []
    
    def learn(self,new_info):
        self.knowledge.append(new_info)