def parent(node, root, first):
    if node >= root:
        return -1
    if node == root - 1 or node == ((root - 1) + first) // 2:
        return root
    elif node > ((root - 1) + first) // 2:
        return parent(node, root - 1, ((root - 1) + first) // 2)
    else:
        return parent(node, ((root - 1) + first) // 2, first)
def solution(h, q):
    return [parent(i, 2 ** h - 1, 0) for i in q]