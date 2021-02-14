import math
import numpy as np
import matrix_multiply as mm

def clockwise_rotation(m_c,m_t,m_rt):
	m1 = mm.matrix_mul(m_rt,m_c)
	m2 = mm.matrix_mul(m1,m_t)
	return m2

def anticlockwise_rotation(m_ac,m_t,m_rt):
	m1 = mm.matrix_mul(m_rt,m_ac)
	m2 = mm.matrix_mul(m1,m_t)
	return m2

def rotation(count,x1,y1,degree):
	a=math.sin(math.radians(degree))
	s=np.around(a,decimals=1)
	b=math.cos(math.radians(degree))
	c=np.around(b,decimals=1)
	m_c = ([c,s,0],[-s,c,0],[0,0,1])
	m_ac = ([c,-s,0],[s,c,0],[0,0,1])
	m_t = ([1,0,-x1],[0,1,-y1],[0,0,1])
	m_rt = ([1,0,x1],[0,1,y1],[0,0,1])
	if count==1 :
		mf=clockwise_rotation(m_c,m_t,m_rt)
	elif count==2 :
		mf=anticlockwise_rotation(m_ac,m_t,m_rt)
	return mf