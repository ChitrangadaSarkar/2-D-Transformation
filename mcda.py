import numpy as np

def midpoint_circle(xc,yc,r):
	X=[0]
	Y=[r]
	x,y=0,r
	p_c=(5/4)-r
	while x<=y:
		if p_c<0:
			p_c=p_c+(2*x)+3
			x=x+1
			if(x>y):
				break
			else:
				X.append(x)
				Y.append(y)
		else:
			p_c=p_c+(2*(x-y))+5
			y=y-1
			x=x+1
			if(x>y):
				break
			else:
				X.append(x)
				Y.append(y)
	X_1=[]
	Y_1=[]
	X_rev = []
	Y_rev = []
	X_rev.extend(Y)
	X_neg = list(map(lambda x:-x, X))
	X_rev_neg = list(map(lambda x:-x,X_rev))
	Y_rev.extend(X)
	Y_neg = list(map(lambda x:-x, Y))
	Y_rev_neg = list(map(lambda x:-x,Y_rev))
	X_new = [X,X_rev[::-1],X_rev,X[::-1],X_neg,X_rev_neg[::-1],X_rev_neg,X_neg[::-1]]
	Y_new = [Y,Y_rev[::-1],Y_rev_neg,Y_neg[::-1],Y_neg,Y_rev_neg[::-1],Y_rev,Y[::-1]]
	for i in X_new :		
		X_1.extend(i)
	for i in Y_new :		
		Y_1.extend(i)
	if xc==0 and yc==0 :
		general_matrix = [[X_1],[Y_1]]
		return general_matrix
	elif xc!=0 or yc!=0 :
		X1 = list(map(lambda x:x+xc,X_1))
		Y1 = list(map(lambda x:x+yc,Y_1))
		general_matrix = [[X1],[Y1]]
		return general_matrix



	
