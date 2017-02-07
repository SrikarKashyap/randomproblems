#Works for both Python 2.7 and 3.5

def matched(string):

	head=-1   #for pointing to the latest bracket (to pop later)
	stack=[]  #LIFO for storing symbols
	for i in string:
		if i=='(': 
			stack.append(i)  #Store ( for later verification of correctness
			head+=1 #Update head to point to next space in the stack

		elif i==')': 
			if not stack:  #Directly return False if the stack is empty
				return False
			elif stack[head]=='(':
				stack.pop()  #Pop the matching expression and decrement head
				head-=1
		else:
			pass
	if not stack:  #Verifying if stack is empty after processing
		return True
	return False #Final case

if __name__ == '__main__':
	s = input()
	print(matched(s))