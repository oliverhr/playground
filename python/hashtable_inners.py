# In a very simpistic way this how a
# hashtable can be implemented

class Entry:
	def __init__(self, k, v):
		self.key = k
		self.value = v

class HashTable:
	def __init__(self, M=25):
		self.M = M
		self.table = [None] * M

	def put(self, k, v):
		hc = hash(k) % self.M
		entry = self.table[hc]
		if entry:
			if entry.key == k:
				entry.value = v
			else:
				raise RuntimeError(f'Key Collision {k} and {entry.key}: {hc}')
		else:
			self.table[hc] = Entry(k,v)

	def get(self, k):
		hc = hash(k) % self.M
		return self.table[hc].value if self.table[hc] else None

def main():
	table = HashTable()
	table.put('Friday',	2)
	table.put('Sunday',	5)
	table.put('Wednesday',	11)

	print(table.get('Friday'))
	print(table.get('Sunday'))
	print(table.get('Saturday'))

if __name__ == '__main__':
	main()
