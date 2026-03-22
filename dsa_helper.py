patterns = {
    "Sliding Window": ["substring", "subarray", "window", "contiguous"],
    "Binary Search": ["sorted", "search", "mid"],
    "Two Pointer": ["pair", "sum", "target"],
    "DFS/BFS": ["graph", "tree", "traverse"],
    "Dynamic Programming": ["maximum", "minimum", "ways", "optimize"]
}

hints = {
    "Sliding Window": "Use two pointers and maintain a moving window.",
    "Binary Search": "Divide the search space into halves.",
    "Two Pointer": "Use two indices moving towards each other.",
    "DFS/BFS": "Traverse nodes using stack (DFS) or queue (BFS).",
    "Dynamic Programming": "Break problem into subproblems and store results."
}

def analyze_problem(text):
    text = text.lower()
    scores = {}

    for pattern, keywords in patterns.items():
        score = 0
        for word in keywords:
            if word in text:
                score += 1
        scores[pattern] = score

    best_pattern = max(scores, key=scores.get)

    if scores[best_pattern] == 0:
        return "Unknown", "No strong keywords found", "Try analyzing constraints."

    return best_pattern, f"Matched {scores[best_pattern]} keyword(s)", hints[best_pattern]


print("=== DSA Pattern Recognizer ===")

while True:
    problem = input("\nEnter your problem (or type 'exit'): ")

    if problem.lower() == "exit":
        break

    pattern, reason, hint = analyze_problem(problem)

    print(f"\nPattern: {pattern}")
    print(f"Reason: {reason}")
    print(f"Hint: {hint}")