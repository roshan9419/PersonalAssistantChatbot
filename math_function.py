import math
def basicOperations(text):
	if 'root' in text:
		temp = text.rfind(' ')
		num = int(text[temp+1:])
		return round(math.sqrt(num),2)

	text = text.replace('plus', '+')
	text = text.replace('minus', '-')
	text = text.replace('x', '*')
	text = text.replace('multiplied by', '*')
	text = text.replace('multiply', '*')
	text = text.replace('divided by', '/')
	text = text.replace('to the power', '**')
	text = text.replace('power', '**')
	result = eval(text)
	return round(result,2)

def bitwiseOperations(text):
	if 'right shift' in text:
		temp = text.rfind(' ')
		num = int(text[temp+1:])
		return num>>1
	elif 'left shift' in text:
		temp = text.rfind(' ')
		num = int(text[temp+1:])
		return num<<1
	text = text.replace('and', '&')
	text = text.replace('or', '|')
	text = text.replace('not of', '~')
	text = text.replace('not', '~')
	text = text.replace('xor', '^')
	result = eval(text)
	return result

def conversions(text):
	temp = text.rfind(' ')
	num = int(text[temp+1:])
	if 'bin' in text:
		return eval('bin(num)')[2:]
	elif 'hex' in text:
		return eval('hex(num)')[2:]
	elif 'oct' in text:
		return eval('oct(num)')[2:]

def trigonometry(text):
	temp = text.replace('degree','')
	temp = text.rfind(' ')
	deg = int(text[temp+1:])
	rad = (deg * math.pi) / 180
	if 'sin' in text:
		return round(math.sin(rad),2)
	elif 'cos' in text:
		return round(math.cos(rad),2)
	elif 'tan' in text:
		return round(math.tan(rad),2)

def factorial(n):
	if n==1 or n==0: return 1
	else: return n*factorial(n-1)

def isHaving(text, lst):
	for word in lst:
		if word in text:
			return True
	return False

def perform(text):
	text = text.replace('math','')
	if "factorial" in text: return str(factorial(int(text[text.rfind(' ')+1:])))
	elif isHaving(text, ['sin','cos','tan']): return str(trigonometry(text))
	elif isHaving(text, ['bin','hex','oct']): return str(conversions(text))
	elif isHaving(text, ['shift','and','or','not']): return str(bitwiseOperations(text))
	else: return str(basicOperations(text))
