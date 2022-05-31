#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

def read_adjacency_matrix(n):
    nodes_dict = dict()

    for i in range(n):
        nodes_dict[i] = [c for c, val in enumerate(input().split()) if int(val) == 1]

    return nodes_dict


def get_weak_vertices(nodes_dict):
    # Verify if the node in the dictionary is weak
    weak_nodes = list()
    for node_id, node_links in nodes_dict.items():
        weak_node = True
        for node_1 in node_links:
            for node_2 in nodes_dict[node_1]:
                if node_2 in node_links:
                    weak_node = False
                    break
            if not weak_node:
                break
        if weak_node:
            weak_nodes.append(node_id)

    return weak_nodes


def main():
    while True:
        a = input()
        n = int(a)
        if n == -1:
            break
        nodes_dict = read_adjacency_matrix(n)
        print(*get_weak_vertices(nodes_dict))


if __name__ == '__main__':
    main()