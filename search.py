#coding=utf-8
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import copy
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST




    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
	
    
    #����������Ҫ�Ľṹ

    from util import Stack
    OpenTable = Stack()
    Path = []
    depth = 0
    CloseTable = set()

	#������ʼ�ڵ�״̬
    start = problem.getStartState()
    
    OpenTable.push((([start,"Stop",0]),0))
    
    poppath = False
    
	#��ʼ����
    while not OpenTable.isEmpty():
		#����ջ���ڵ�
        node = OpenTable.pop()
		
		#�ж��Ƿ���ʹ�
        if node[0][0] in CloseTable:
            continue
		
		#�ýڵ����
        depth = node[1]
		
		#����һ�����ʽڵ�û�к�̽ڵ㣬�����Pathά��
        if poppath:
            Path = Path[0:depth]
	
		#���ýڵ���Ϊ����
        CloseTable.add(node[0][0])
		
		#׷��·��
        Path.append(node[0][1])

		
		#�ж��Ƿ���Ŀ��ڵ�
        if problem.isGoalState(node[0][0]):
	    Path = Path[1:]
            return Path
        
		
		#�ӽڵ���Ҫ���+1
        depth+=1
		
		#��չ�ýڵ�
        poppath = True
        for successor in problem.getSuccessors(node[0][0]):
            if successor[0] not in CloseTable:
                OpenTable.push((successor,depth))
                poppath = False

                
        
      
                

    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
	
	#������Ҫ�Ľṹ
    from util import Queue
    OpenTable = Queue()
    Path = []
    CloseTable = set()

	#��ȡ��ʼ����
    start = problem.getStartState()

	#ѹ���һ���ڵ�
    OpenTable.push((([start,"Stop",0]),[]))
    
	#��ʼ����
    while not OpenTable.isEmpty():
		
        node = OpenTable.pop()
       	
       	if node[0][0] in CloseTable:
            continue
			
		#��ΪlistΪ�ɱ������������Ҫ���
        temp = copy.deepcopy(node[1])
		
		
        CloseTable.add(node[0][0])
        temp.append(node[0][1])

		#�ж��Ƿ���Ŀ��ڵ�
        Path = temp		
        if problem.isGoalState(node[0][0]):
            Path = Path[1:]
            return Path
        

        
       
		#��չ�ڵ�
        for successor in problem.getSuccessors(node[0][0]):
            
            if successor[0] not in CloseTable:
                OpenTable.push((successor,temp))
                

                
        
      
                

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
	#������Ҫ�Ľṹ
    from util import PriorityQueue
    OpenTable = PriorityQueue()
    Path = []
    CloseTable = set()
	
	#��ȡ��ʼ������
    start = problem.getStartState()

	#ѹ���һ���ڵ㣬��һ���ڵ�����ֵ��Ϊ0
    OpenTable.push((([start,"Stop",0]),[]),0)
	
	#��ʼ����
    while not OpenTable.isEmpty():
		node = OpenTable.pop()
		
		if node[0][0] in CloseTable:
				continue
				
		tmp = copy.deepcopy(node[1])
		
		CloseTable.add(node[0][0])
		tmp.append(node[0][1])
			
		#�ж��Ƿ���Ŀ��ڵ�
		Path = tmp
		if problem.isGoalState(node[0][0]):
			Path = Path[1:]
			return Path
		
		#��չ�ýڵ�
		for successor in problem.getSuccessors(node[0][0]):
			if successor[0] not in CloseTable:
				#��������ֵ
				cost = successor[2]+node[0][2]
				pushsu = (successor[0],successor[1],cost)
				OpenTable.push((pushsu,tmp),cost)

    return []
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
	#������Ҫ�Ľṹ
    from util import PriorityQueue
    OpenTable = PriorityQueue()
    Path = []
    CloseTable = set()
	
	
    start = problem.getStartState()
	#ѹ���һ���ڵ㣬��һ���ڵ�����ֵ��Ϊ0
    OpenTable.push((([start,"Stop",0]),[]),0)
	
	#��ʼ����
    while not OpenTable.isEmpty():
        node = OpenTable.pop()
		
	if node[0][0] in CloseTable:
		continue
			
        tmp = copy.deepcopy(node[1])
		
        CloseTable.add(node[0][0])
		
        tmp.append(node[0][1])

		
        Path = tmp
        if problem.isGoalState(node[0][0]):
	       Path = Path[1:]
	       return Path
		   
		#��չ�ýڵ�
        for successor in problem.getSuccessors(node[0][0]):
               if successor[0] not in CloseTable:
                    cost = successor[2] + node[0][2]#��ʼ�㵽�ýڵ��ʵ�ʴ���
                    pushsu = (successor[0],successor[1],cost)
                    h = heuristic(successor[0],problem)#�ýڵ㵽Ŀ��ڵ�Ĺ�ֵ
                    fn = cost + h#����֮����Ϊ����ֵ
                    OpenTable.push((pushsu,tmp),fn)
    return [] 


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
