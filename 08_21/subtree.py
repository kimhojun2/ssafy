def sub_tree(node):
    global cnt
    for i in range(2):
        if tree[i][node]:
            cnt += 1
            n = tree[i][node]
            sub_tree(n)

T = int(input())
for tc in range(1, T+1):
    E, N = map(int,input().split())
    temp = input().split()
    # 노드번호는 1번부터 E+1번까지 존재 -> 이진트리 리스트 초기화
    tree = [[0for _ in range(E+2)] for _ in range(2)]
    for i in range(E):
        p_node = int(temp[2*i])
        c_node = int(temp[2*i+1])
        if tree[0][p_node] == 0:    # 왼쪽 자식이 없다면 할당, 왼쪽 자식이 있다면 오른쪽에 할당
            tree[0][p_node] = c_node
        else:
            tree[1][p_node] = c_node

    cnt = 1
    sub_tree(N)
    print(f'#{tc} {cnt}')
