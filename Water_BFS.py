from collections import deque
def bfs(a, b, target):

	m = {}
	isSolvable = False
	path = []


	q = deque()

	q.append((0, 0))

	while (len(q) > 0):
		u = q.popleft()# If this state is already visited
		if ((u[0], u[1]) in m):
			continue
		if ((u[0] > a or u[1] > b or
			u[0] < 0 or u[1] < 0)):
			continue

		# Filling the vector for constructing
		# the solution path
		path.append([u[0], u[1]])

		# Marking current state as visited
		m[(u[0], u[1])] = 1

		# If we reach solution state, put ans=1
		if (u[0] == target or u[1] == target):
			isSolvable = True

			if (u[0] == target):
				if (u[1] != 0):

					# Fill final state
					path.append([u[0], 0])
			else:
				if (u[0] != 0):

					# Fill final state
					path.append([0, u[1]])

			return path
			

		# If we have not reached final state
		# then, start developing intermediate
		# states to reach solution state
		q.append([u[0], b]) # Fill Jug2
		q.append([a, u[1]]) # Fill Jug1
		
		c,d=u[0],u[1]
		
		while(c<a and d>0):
		    c+=1
		    d-=1
		q.append([c,d])
		
		while(c>0 and d<b):
		    c-=1
		    d+=1
		q.append([c,d])
		q.append([a, 0])

		# Empty Jug1
		q.append([0, b])

	# No, solution exists if ans=0
	if (not isSolvable):
		return[-1]

x=int(input("Enter Jug 1: "))
y=int(input("Enter Jug 2: "))
z=int(input("Enter Target: "))

a=bfs(x,y,z)
b=bfs(y,x,z)

if(len(a) <= len(b)):
	for x in a:
		print(x)
else:
	for x in b:
		print(b)

