# -*- coding: utf-8 -*-

a = {
     '朱承浩':{'name':'朱承浩','username':'zhu','age':19},
     '赵老板':{'name':'赵老板','username':'zhao','age':20}
}


def search_function(name=None, type=None):
  if(type is None):
      return a[name]
  else:
      return a[name][type]


name = search_function(name='朱承浩',type="name")
print name
