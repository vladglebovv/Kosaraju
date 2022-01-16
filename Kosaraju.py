from random import randint
import time

def get_graph():
	global vv
	global V
	global VR
	for i in range(n):
		V[randint(0, n-1)].append(vv.pop())
	
	for vertex, edges in enumerate(V):
		for u in edges:
			VR[u].append(vertex)

def dfs():
	for vertex in range(len(VR)):
		if visited[vertex] == False:
			explore(vertex)

def explore(vertex):
	visited[vertex] = True
	previsit(vertex)
	for u in VR[vertex]:
		if visited[u] == False:
			explore(u)
	postvisit(vertex)

def previsit(vertex):
	global clock
	pre[vertex] = clock
	clock += 1

def postvisit(vertex):
	global clock 
	post[vertex] = clock
	post_sorted.append(vertex) 
	clock += 1

def ccdfs():
	global clock 
	global pre 
	global post 
	global visited
	clock = 1
	pre, post = [-1]*n, [-1]*n
	visited = [False]*n
	cc = 0
	for vertex in post_sorted:
		if visited[vertex] == False:
			cc += 1
			ccexplore(vertex, cc)

def ccexplore(vertex, cc):
	visited[vertex] = True
	ccprevisit(vertex, cc)
	for u in V[vertex]:
		if visited[u] == False:
			ccexplore(u, cc)
	ccpostvisit(vertex, cc)
	
def ccprevisit(vertex, cc):
	global clock 
	pre[vertex] = clock
	clock += 1
	ccnum[vertex] = cc

def ccpostvisit(vertex, cc):
	global clock 
	post[vertex] = clock 
	if cc not in t_sorted:
		t_sorted[cc] = post[vertex]
	elif post[vertex] > t_sorted[cc]:
		t_sorted[cc] = post[vertex]
	clock += 1

x,y=[],[]
for n in range(1000, 10000, 1000):
	res = []
	for i in range(100):
		vv = list(range(n))
		visited, pre, post, ccnum = [False]*n, [-1]*n, [-1]*n, [-1]*n
		clock = 1
		post_sorted = []
		t_sorted = dict()
		V = [[] for vertex in range(n)]
		VR = [[] for vertex in range(n)]

		get_graph()
		start_time = time.time()
		dfs()
		post_sorted = post_sorted[::-1]
		ccdfs()
		res.append(time.time() - start_time)
		#print(list(zip(pre, post)))
		#print(post_sorted)
		#print(ccnum)
		#print(t_sorted)
	y.append((sum(res)/100*1000))
	x.append(n)
print('-----------------------------')
print(x)
print(y)
