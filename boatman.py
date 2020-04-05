# Import the pygame module
import pygame
from collections import deque 
# Import random for random numbers
import random
clock = pygame.time.Clock()
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class State(object):
    def __init__(self, state=None):
        
        if state == None:
            state = "0"
        self.__state = state 
    
    def generate_next_state(self):
        child_states = []

        if self.__state ==  "0":
            child_states.append("9") 
            ''' man with goat ''' 

        elif self.__state == "1":
            child_states.append("9") 
            ''' man alone '''
            child_states.append("13") 
            ''' man with wolf '''
            child_states.append("11") 
            ''' man with cabbage ''' 

        elif self.__state == "2":
            child_states.append("14") 
            ''' man with wolf '''
            child_states.append("11") 
            ''' man with goat ''' 

        elif self.__state == "4":
            child_states.append("14") 
            ''' man with cabbage ''' 
            child_states.append("13") 
            ''' man with goat ''' 

        elif self.__state == "6":
            child_states.append("14") 
            ''' man alone '''
            child_states.append("15") 
            ''' man with goat ''' 

        elif self.__state == "9":
            child_states.append("1") 
            ''' man alone '''
            child_states.append("0") 
            ''' man with goat ''' 

        elif self.__state == "11":
            child_states.append("3") 
            ''' man alone '''
            child_states.append("1") 
            ''' man with cabbage ''' 
            child_states.append("2") 
            ''' man with goat ''' 

        elif self.__state == "13":
            child_states.append("5") 
            ''' man alone '''
            child_states.append("4") 
            ''' man with goat ''' 
            child_states.append("1") 
            ''' man with wolf ''' 
        elif self.__state == "14":
            child_states.append("6") 
            ''' man alone '''
            child_states.append("4") 
            ''' man with cabbage ''' 
            child_states.append("2") 
            ''' man with wolf ''' 

        return child_states

class Visual_node(pygame.sprite.Sprite):
    def __init__(self, x, y, value, img_name=None):
        super(Visual_node, self).__init__()
        self.surf = pygame.Surface((24, 24))
        if img_name == None:
            self.surf.fill((255, 255, 255))
        else:
            self.surf = pygame.image.load(img_name).convert()
        self.value = value
        self.next_states = State(value).generate_next_state()
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect(
            center=(
                x,
                y,
            )
        )

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

node0 = Visual_node(400, 10, "0", "0.png")
node1 = Visual_node(300, 70, "1", "1.png")
node2 = Visual_node(500, 70, "2", "2.png")
node3 = Visual_node(200, 150, "3","3.png")
node4 = Visual_node(600, 150, "4", "4.png")
node5 = Visual_node(410, 150, "5", "5.png")
node6 = Visual_node(120, 260, "6", "6.png")
node7 = Visual_node(340, 255, "7", "7.png")
node8 = Visual_node(550, 265, "8", "8.png")
node9 = Visual_node(690, 260, "9", "9.png")
node10 = Visual_node(50, 350, "10")
node11 = Visual_node(200, 350, "11")
node12 = Visual_node(450, 355, "12")
node13 = Visual_node(600, 357, "13")
node14 = Visual_node(250, 450, "14")
node15 = Visual_node(580, 450, "15")

all_nodes = pygame.sprite.Group()
all_edges = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_nodes.add(node0)
all_sprites.add(node0)

all_nodes.add(node1)
all_sprites.add(node1)

all_nodes.add(node2)
all_sprites.add(node2)

all_nodes.add(node3)
all_sprites.add(node3)

all_nodes.add(node4)
all_sprites.add(node4)

all_nodes.add(node5)
all_sprites.add(node5)

all_nodes.add(node6)
all_sprites.add(node6)

all_nodes.add(node7)
all_sprites.add(node7)

all_nodes.add(node8)
all_sprites.add(node8)

all_nodes.add(node9)
all_sprites.add(node9)

all_nodes.add(node10)
all_sprites.add(node10)

all_nodes.add(node11)
all_sprites.add(node11)

all_nodes.add(node12)
all_sprites.add(node12)

all_nodes.add(node13)
all_sprites.add(node13)

all_nodes.add(node14)
all_sprites.add(node14)

all_nodes.add(node15)
all_sprites.add(node15)


class Graph(object):
    def __init__(self, graph_dict=None, list_invalid=None):
        '''
        if no dictornary given, empty dictonary created
        '''
        if list_invalid == None:
            list_invalid = ["3", "5", "7", "8", "10", "12"]
        if graph_dict == None:
            s = State()
            child = s.generate_next_state()
            graph_dict = {}
            for c in child:
                if "0" in graph_dict:
                    graph_dict["0"].append(c) 
                else:
                    graph_dict["0"] = [c]
                if c in graph_dict:
                    graph_dict[c].append("0")
                else:
                    graph_dict[c] = ["0"]

           

        self.__graph_dict = graph_dict
        self.__list_invalid = list_invalid

    def vertices(self):
        '''
        returns the vertices of the graph
        '''
        return list(self.__graph_dict.keys())
    
    def edges(self):
        '''
        returns the edges of the graph
        '''
        return self.__generate_edges()
    
    def add_vertex(self, vertex):
        '''
        if vertex not present in graph, add, else do nothing
        '''
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
    
    def add_edge(self, edge):
        '''
        assuming edge is of type set, tuple or list
        '''
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
    
    def __generate_edges(self): 
        '''
        class function
        represented as sets
        '''
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges 
    
    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res 
    
    def find_path(self, start_vertex, end_vertex, path=None):
        graph = self.__graph_dict
        if path == None:
            path = []
        path.append(start_vertex)
        if start_vertex == end_vertex:
            return path 
        if start_vertex not in graph:
            return None 
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)

                if extended_path:
                    return extended_path
        return None 

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths

    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
            it, i.e. the number of adjacent vertices. Loops are counted 
            double, i.e. every occurence of vertex in the list 
            of adjacent vertices. """ 
        adj_vertices =  self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

            
    def find_isolated_vertices(self):
        """ returns a list of isolated vertices. """
        graph = self.__graph_dict
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

    def delta(self):
        """ the minimum degree of the vertices """
        min = 100000000
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < min:
                min = vertex_degree
        return min
        
    def Delta(self):
        """ the maximum degree of the vertices """
        max = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max

    def BFS(self, start_vertex, goal_vertex):
        q = deque()
        q.append(start_vertex)
        visited = []
        explored = []
        graph = self.__graph_dict
        
        while q:
            v = q.popleft()

                
            starter_children = []
            starter_children = State(v).generate_next_state()
            for child in starter_children:
                if v not in graph:
                    graph[v] = child
                else:
                    graph[v].append(child)
                if child not in graph:
                    graph[child] = [v]
                else:
                    graph[child].append(v)

                visited.append(v)
                print("mother node " + v)
                print("\n")
                
               

            for neighbour in graph[v]:
                if neighbour not in visited and neighbour not in explored:
                    if neighbour not in self.__list_invalid:
                        q.append(neighbour)
                        explored.append(neighbour)
                        print("child nodes " + neighbour)
                    if neighbour == goal_vertex:
                        print("found ")
                        return explored
                    else:
                        pass 


class Visual_graph(pygame.sprite.Sprite):
    def __init__(self, st_node, end_node):
        super(Visual_graph, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.surf.fill((255, 0, 0))
        self.st = int(st_node)
        self.en = int(end_node)
        self.explored = Graph().BFS(st_node, end_node)
            
    def update(self, screen):
        for node in all_nodes:
            screen.blit(node.surf, node.rect)
            children = node.next_states
            for child in children:
                for c in all_nodes:
                    if child == c.value:
                        
                        pygame.draw.line(screen, (255, 255, 255), (node.x, node.y), (c.x, c.y))
    def visual_bfs(self, no_of_node):
        done = []
        i = 0
        for node in self.explored:
            for c in all_nodes:
                if node == c.value and c not in done and i < no_of_node:
                  c.surf.fill((0,0,255))
                  done.append(c) 
                  i += 1
                  print(c.value)
                
                
                    
                
                

 



g = Visual_graph("0", "15")

# Create a custom event for node coloring 
COLORNODE = pygame.USEREVENT + 1
pygame.time.set_timer(COLORNODE, 250)

running = True
no_of_node = 1
while running:

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False
        elif event.type == COLORNODE:
            no_of_node += 1
            

        
        screen.fill((0, 220, 255))
        
        
        
        
        
        
        g.update(screen)
        
        

        g.visual_bfs(no_of_node)
        

        

        pygame.display.flip()


