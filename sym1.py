import sympy as sp
import re

# Define symbols
x, y, z = sp.symbols('x y z')

# Function to parse math expressions from text
def parse_math_query(query):
    query = query.lower().strip()
    
    try:
        if "differentiate" in query or "derivative" in query:
            match = re.search(r'differentiate (.+) with respect to (.+)', query)
            if match:
                expr = sp.sympify(match.group(1))
                var = sp.symbols(match.group(2))
                return sp.diff(expr, var)
        
        elif "integrate" in query or "integral" in query:
            match = re.search(r'integrate (.+) with respect to (.+)', query)
            if match:
                expr = sp.sympify(match.group(1))
                var = sp.symbols(match.group(2))
                return sp.integrate(expr, var)
        
        elif "solve" in query:
            match = re.search(r'solve (.+) for (.+)', query)
            if match:
                expr = sp.sympify(match.group(1))
                var = sp.symbols(match.group(2))
                return sp.solve(expr, var)
        
        elif "expand" in query:
            match = re.search(r'expand (.+)', query)
            if match:
                expr = sp.sympify(match.group(1))
                return sp.expand(expr)
        
        elif "factor" in query:
            match = re.search(r'factor (.+)', query)
            if match:
                expr = sp.sympify(match.group(1))
                return sp.factor(expr)
        
        return "Invalid query. Use 'differentiate', 'integrate', 'solve', 'expand', or 'factor'."
    except Exception as e:
        return f"Error processing query: {e}"

# Simulated test cases
def run_test_cases():
    test_queries = [
        "Differentiate x**2 + 3*x with respect to x",
        "Integrate sin(x) with respect to x",
        "Solve x**2 - 4 for x",
        "Expand (x + y)**2",
        "Factor x**2 - 9",
        "Differentiate e**x with respect to x",
        "Integrate x**3 with respect to x"
    ]
    
    for query in test_queries:
        print(f"Query: {query}")
        print("Result:", parse_math_query(query))
        print("-")

if __name__ == "__main__":
    print("Running test cases...")
    run_test_cases()
