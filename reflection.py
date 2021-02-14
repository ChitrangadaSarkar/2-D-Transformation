import math
import numpy as np
import matrix_multiply as mm

def x_axis():
	m1 = ([1,0,0],[0,-1,0],[0,0,1])
	return m1

def y_axis():
	m1 = ([-1,0,0],[0,1,0],[0,0,1])
	return m1

def x_parallel(cst):
	if cst>0 :
		m1 = ([1,0,0],[0,1,cst],[0,0,1])
		m2 = ([1,0,0],[0,-1,0],[0,0,1])
		m3 = ([1,0,0],[0,1,-cst],[0,0,1])
		m4 = np.dot(m1,m2)
		m5 = np.dot(m4,m3)
	else :
		m1 = ([1,0,0],[0,1,-cst],[0,0,1])
		m2 = ([1,0,0],[0,-1,0],[0,0,1])
		m3 = ([1,0,0],[0,1,cst],[0,0,1])
		m4 = np.dot(m1,m2)
		m5 = np.dot(m4,m3)
	return m5

def y_parallel(cst):
	if cst>0 :
		m1 = ([1,0,cst],[0,1,0],[0,0,1])
		m2 = ([-1,0,0],[0,1,0],[0,0,1])
		m3 = ([1,0,-cst],[0,1,0],[0,0,1])
		m4 = np.dot(m1,m2)
		m5 = np.dot(m4,m3)
	else :
		m1 = ([1,0,-cst],[0,1,0],[0,0,1])
		m2 = ([-1,0,0],[0,1,0],[0,0,1])
		m3 = ([1,0,cst],[0,1,0],[0,0,1])
		m4 = np.dot(m1,m2)
		m5 = np.dot(m4,m3)
	return m5

def others(cst, m):
    degree = math.degrees(math.atan(m))
    a = math.sin(math.radians(degree))
    s = np.around(a, decimals=1)
    a = math.cos(math.radians(degree))
    c = np.around(a, decimals=1)
    m_c = ([c, s, 0], [-s, c, 0], [0, 0, 1])
    m_x = ([1, 0, 0], [0, -1, 0], [0, 0, 1])
    m_ac = ([c, -s, 0], [s, c, 0], [0, 0, 1])
    m_t1 = ([1, 0, -cst], [0, 1, 0], [0, 0, 1])
    m_t2 = ([1, 0, cst], [0, 1, 0], [0, 0, 1])
    if cst == 0:
        m1 = mm.matrix_mul(m_ac, m_x)
        mf = mm.matrix_mul(m1, m_c)
    elif cst > 0:
        m1 = mm.matrix_mul(m_t2, m_ac)
        m2 = mm.matrix_mul(m1, m_x)
        m3 = mm.matrix_mul(m2, m_c)
        mf = mm.matrix_mul(m3, m_t1)
    else:
        m1 = mm.matrix_mul(m_t1, m_ac)
        m2 = mm.matrix_mul(m1, m_x)
        m3 = mm.matrix_mul(m2, m_c)
        mf = mm.matrix_mul(m3, m_t2)
    return mf
