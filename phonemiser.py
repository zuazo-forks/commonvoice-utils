import re 


class Phonemiser:
	"""
	>>> p = Phonemiser('ab')
	>>> p.phonemise('гӏапынхъамыз')
	'ʕapənqaməz'
	"""
	def __init__(self, lang):
		self.lang = lang

		self.load_data()

	def load_data(self):
		self.lkp = {}
		for line in open('data/' + self.lang + '/phon.tsv').readlines():
			row = line.strip('\n').split('\t')
			k = row[0].strip()	
			v = row[1].strip()	
			if k not in self.lkp:
				self.lkp[k] = []
			self.lkp[k].append(v)
		
	def maxmatch(self, token):
		token += ' '

		if token.strip() == '':
			return []

		dictionary = self.lkp.keys()
	
		for i in range(0, len(token)+1):
			firstWord = token[0:-i]
			remainder = token[-i:]
			if firstWord in dictionary:
				return [firstWord] + self.maxmatch(remainder)
	
		firstWord = token[0]
		remainder = token[1:]
	
		return [firstWord] + self.maxmatch(remainder)
	
	def phonemise(self, token):
		ks = list(self.lkp.keys())
		ks.sort(key=lambda x : len(x), reverse=True)
		segs = self.maxmatch(token.lower())	
		op = ''
		for seg in segs:
			if seg in self.lkp:
				op += self.lkp[seg][0]
		return op
	
if __name__ == "__main__":
	import doctest
	doctest.testmod()
