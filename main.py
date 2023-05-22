from queue import Queue
from graphviz import Digraph
import os
import copy


class Node:
    def __init__(self, state, parent, action, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.id = "".join(str(n) for n in self.state)

    def __repr__(self):
        joined_string = " ".join(str(n) for n in self.state)
        return joined_string[0:5]+"\n"+joined_string[6:11]+"\n"+joined_string[12:17]


def possible_moves(state):
    pos_moves = []
    empty_index = state.index(0)
    if empty_index not in [0, 1, 2]:  # Up
        pos_moves.append('Up')
    if empty_index not in [6, 7, 8]:  # Down
        pos_moves.append('Down')
    if empty_index not in [0, 3, 6]:  # Left
        pos_moves.append('Left')
    if empty_index not in [2, 5, 8]:  # Right
        pos_moves.append('Right')
    return pos_moves
    return pos_moves

def generate_state(state, move):
    empty_index = state.index(0)
    new_state = state[:]
    if move == 'Up':
        new_state[empty_index], new_state[empty_index - 3] = new_state[empty_index - 3], new_state[empty_index]
    elif move == 'Down':
        new_state[empty_index], new_state[empty_index + 3] = new_state[empty_index + 3], new_state[empty_index]
    elif move == 'Left':
        new_state[empty_index], new_state[empty_index - 1] = new_state[empty_index - 1], new_state[empty_index]
    elif move == 'Right':
        new_state[empty_index], new_state[empty_index + 1] = new_state[empty_index + 1], new_state[empty_index]
    return new_state


def create_node(state, parent, action, depth):
    return Node(state, parent, action, depth)


def expand_node(node):
    expanded_nodes = []
    for move in possible_moves(node.state):
        expanded_nodes.append(create_node(generate_state(node.state, move), node.id, move, node.depth + 1))
    return expanded_nodes


def dfs():
    stack = []
    visited = []
    visited_str = []
    depth_limit = 5
    stack.append(create_node(initial, "283164705", None, 0))
    while len(stack) > 0:
        node = stack.pop(0)
        if node.id in visited_str:
            continue
        else:
            visited.append(node)
            visited_str.append(node.id)

        if node.state == goal:
            return visited

        if node.depth < depth_limit:
            expanded_nodes = expand_node(node)
            if (expanded_nodes not in visited):
                expanded_nodes.extend(stack)
                stack = expanded_nodes


def bfs():
    queue = []
    visited = []
    visited__str = []
    depth__limit = 5
    queue.append(create_node(initial, "283164705", None, 0))
    while(len(queue)>0):
        node = queue.pop()
        if node.id in visited__str:
            continue
        else:
            visited.append(node)
            visited__str.append(node.id)
            if node.state == goal:
                return visited
            if node.depth < depth__limit:
                expanded__nodes = expand_node(node)
                if(expanded__nodes not in visited):
                    expanded__nodes.extend(queue)
                    queue = expanded__nodes
        if(len(queue)==0): return None



def display(title, path, file):
    graph = Digraph(comment=title)
    step = 0

    for node in path:
        node_str = node.__str__()
        color = "black"

        if node.state == goal:
            color = "green"

        graph.node(str(node.id), node_str, color=color)

        if node.parent:
            graph.edge(str(node.parent), str(node.id), str(node.action) + "\n" + str(step))
            step += 1

    output_file = os.path.join(os.getcwd(), 'outputs', file + '.gv')
    graph.render(output_file, view=True)


def astar():
    # to do
    return 0


def cout(node, goal):
    # to do
    a = 0
    return a




goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
initial = [2, 8, 3, 1, 6, 4, 7, 0, 5]

print(possible_moves(initial))
print(generate_state(initial, 'up'))
print("dfs : ")
print(dfs())
print("bfs : ")
print(bfs())

display("DFS Graph", dfs(), "dfs")

# display("A star graph", astar(), "astar")
# display("Best First graph", bestFirst(), "bf")
# print(bestFirst())
#display("DFS graph", dfs(), "dfs")
# print("dfs : ")

display("BFS graph", bfs(), "bfs")