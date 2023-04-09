import copy  # Includes the deepcopy function for deep copying objects

# Grammar for 0^i 1^i, i >= 1 in Chomsky Normal Form
V1 = ["S", "A", "B", "C"]
Sigma1 = ["0", "1"]
R1 = { 
    "S" : [ ["C", "B"], ["A", "B"] ],
    "C" : [ ["A", "S"]],
    "A" : [["0"]],
    "B" : [["1"]]
}
S1 = "S"
grammar1 = (V1, Sigma1, R1, S1)

# Grammar for balanced parens (excluding epsilon) NOT in Chomsky Normal Form
V2 = ["S"]
Sigma2 = ["(", ")"]
R2 = {"S": [["S", "S"], ["(", "S", ")"], ["(", ")"]]}
S2 = "S"
grammar2 = (V2, Sigma2, R2, S2)

# Grammar from example in Handout 6 
V3 = ["S", "A", "B"]
Sigma3 = ["a", "b"]
R3 = {"S": [["A", "S", "A"], ["a", "B"], ["A"]],
     "A": [["B"], ["S"]],
     "B": [["b"]]}
S3 = "S"
grammar3 = (V3, Sigma3, R3, S3)

def parse(grammar, string):
    """ Takes as input a grammar G = (V, Sigma, R, S) and a string and 
    returns a tuple (Boolean, ParseTree).  If the string is not in the 
    language of the grammar, then this Function returns (False, None).  
    If the string is in the language of the grammar, the function
    returns (True, ParseTree) where ParseTree is a ParseTree for that
    string. A ParseTree is either of the form (Variable, Left, Right) where
    Variable is a variable in the grammar and Left and Right are themselves
    parse trees or (Variable, terminal). """

    cnfGrammar = cnf(grammar)
    V, Sigma, R, S = cnfGrammar
    return cyk(R, S, string, {})

def cyk(rules, variable, string, memo):
    """ Takes grammar rules in Chomsky Normal Form, a variable in that 
    grammar,a string to parse, and a memo dictionary and returns True if the
    string is derivable beginning with that variable and False otherwise. """

    if (variable, string) in memo: return memo[(variable, string)]
    elif len(string) == 1 and [string] in rules[variable]: return True
    else:
        for i in range(1, len(string)):
            left = string[:i]
            right = string[i:]
            for item in rules[variable]:
                if len(item) == 2:  # rhs of rule is of form XY
                    variable1 = item[0]
                    variable2 = item[1]
                    if cyk(rules, variable1, left, memo) and \
                       cyk(rules, variable2, right, memo):
                        memo[(variable, string)] = True
                        return True
        memo[(variable, string)] = False
        return False

def cnf(grammar):
    """ A grammar is a four tuple (V, Sigma, R, S) where V is a a list
    of variables (each is a string of length 1), Sigma is an alphabet,
    R is the rules dictionary with keys from V and values comprising a 
    list of tuples, and S is a string (of length 1) representing the 
    start symbol. Returns a grammar in Chomsky Normal Form. """

    V, Sigma, R, S = grammar
    # Make deep copies of V and R since we'll be modifying these.
    newV = copy.deepcopy(V)
    newR = copy.deepcopy(R)

    return None  # Change this to return a CNF grammar


    
