import re

class FOPCParser:
    def __init__(self):
        self.variables = set()
        self.predicates = set()
    
    def parse_expression(self, expression):
        expression = expression.replace(" ", "")
        pattern = r"(\w+)\((.*?)\)|(\w+)\s*\((.*?)\)"
        matches = re.findall(pattern, expression)
        
        parsed_expressions = []
        for match in matches:
            if match[0]:
                predicate = match[0]
                args = match[1].split(',')
                self.predicates.add(predicate)
                parsed_expressions.append((predicate, args))
            elif match[2]:
                predicate = match[2]
                args = match[3].split(',')
                self.predicates.add(predicate)
                parsed_expressions.append((predicate, args))
        
        return parsed_expressions

    def evaluate_expression(self, expression):
        parsed = self.parse_expression(expression)
        print("Parsed Expressions:")
        for predicate, args in parsed:
            print(f"Predicate: {predicate}, Arguments: {args}")

    def add_variable(self, variable):
        self.variables.add(variable)

    def list_variables(self):
        return list(self.variables)

    def list_predicates(self):
        return list(self.predicates)
if __name__ == "__main__":
    parser = FOPCParser()
    
    expression = "P(x, y) ∧ Q(y, z) ∨ R(z)"
    parser.evaluate_expression(expression)
    parser.add_variable('x')
    parser.add_variable('y')
    parser.add_variable('z')
    
    print("\nVariables:")
    print(parser.list_variables())
    
    print("\nPredicates:")
    print(parser.list_predicates())
