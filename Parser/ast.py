class Node: 
    pass



class NumberNode(Node):
    def __init__(self, val):
        self.val = val

    def __repr__(self) -> str:
        return f"(Number: {self.val})"



class UnaryOpNode(Node):
    def __init__(self, val, op="+"):
        self.op  = op
        self.val = val
    
    def __repr__(self) -> str:
        return f"(Unary: {self.op}{self.val})"



class BinaryOpNode(Node):
    def __init__(self, left, op, right):
        self.left  = left
        self.op    = op
        self.right = right
    
    def __repr__(self) -> str:
        return f"({self.left}, {self.op}, {self.right})"



class MethodCallNode(Node):
    def __init__(self, method, args):
        self.args   = args
        self.method = method
    
    def __repr__(self) -> str:
        return f"(Call {self.method} with {self.args})"
