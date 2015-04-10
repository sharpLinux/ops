#!/usr/bin/python2.7
class Tree:
    def __init__(self, data):
        self.value = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
    def get(self):
	ret = self.children
	ret = filter(lambda s: not s.children, ret)
	for r in ret:
	    print r.value
    def show(self, space):
	print ' '*space, self.value
	for r in self.children:
	    r.show(space+2)
def main():
  a1 = Tree('A-1')
  a2 = Tree('A-2')
  b1 = Tree('B-1')
  b2 = Tree('B-2')
  a1.add_child(b1)
  a2.add_child(b2)
  a2.add_child(Tree('B-3'))
  b2.add_child(Tree('C-1'))
  b2.add_child(Tree('C-2'))
  a1.get()
  b2.get()
  print "Tree a1:"
  a1.show(0)
  print "Tree a2:"
  a2.show(0)

if __name__ == '__main__':
  main()
