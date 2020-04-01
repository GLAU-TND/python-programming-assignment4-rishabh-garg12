A = [('a', 1), ('a', 3), ('a', 5),
('b', 2), ('b', 6),
('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
('d', 4), ('d', 5), ('d', 6), ('d', 7),
('e', 1), ('e', 3), ('e', 5), ('e', 6)]
B = {A[i][1] for i in range(3)}
C = {A[i][1] for i in range(3,5)}
D = {A[i][1] for i in range(5,10)}
E = {A[i][1] for i in range(10,14)}
F = {A[i][1] for i in range(14,18)}
G = [B, C, D, E, F]
K = ['a', 'b', 'c', 'd', 'e']
H = [1,2,3,4]
I = []
for j in range(4):
    H[j] = G[0].union(G[j + 1])
    I.append(len(H[j]))
J = I.index(min(I))
print([('a',K[J + 1])])
