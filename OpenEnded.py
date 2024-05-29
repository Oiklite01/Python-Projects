n= int(input("Enter number of Delgegates from Country A: "))
m= int(input("Enter number of Delgegates from Country B: "))
k= int(input("Enter number of Pairs: "))
link = [0] * (m + 1)
mp = [[0] * (m + 1) for _ in range(n + 1)]

def find(x):
    for dlgt in range(1, m + 1):
        if not vis[dlgt] and mp[x][dlgt]:
            vis[dlgt] = True
            if link[dlgt] == 0 or find(link[dlgt]):
                link[dlgt] = x
                return True
    return False

for _ in range(k):
    s, t = map(int, input().split())
    mp[s][t] = 1

ans = 0
for i in range(1, n + 1):
    vis = [False] * (m + 1)
    if find(i):
        ans += 1

print("minimum number of connections required = ",(n+m-ans))