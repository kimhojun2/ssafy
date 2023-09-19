# 이진트리


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, childNode):
        if not self.left:
            self.left = childNode
            return

        if not self.right:
            self.right = childNode
            return

        return

    # 전위 순회
    # def preorder(self):
    #     # 아무것도 없는 트리를 조회할 때
    #     if self != None:
    #         print(self.value, end=' ')
    #         if self.left:
    #             self.left.preorder()
    #         if self.right:
    #             self.right.preorder()

    # 중위 순회
    # def preorder(self):
    #     # 아무것도 없는 트리를 조회할 때
    #     if self != None:
    #
    #         if self.left:
    #             self.left.preorder()
    #         print(self.value, end=' ')
    #
    #         if self.right:
    #             self.right.preorder()

    # 후위 순회
    def preorder(self):
        # 아무것도 없는 트리를 조회할 때
        if self != None:

            if self.left:
                self.left.preorder()

            if self.right:
                self.right.preorder()

            print(self.value, end=' ')


arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]

nodes = [TreeNode(i) for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].insert(nodes[childNode])

nodes[1].preorder()