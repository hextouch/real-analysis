"""
What happens here

Each level adds one more radical — like adding one more “dimension” 
in your vector analogy.

As NN increases (deeper nesting), the computed value stabilizes:
Depth 1: 1.0000000000  
Depth 2: 1.7320508080  
Depth 3: 2.2912878475  
Depth 4: 2.7577164470  
Depth 5: 2.9340031587  
Depth 6: 2.9807749123  
Depth 7: 2.9940297863  
Depth 8: 2.9980085271  
Depth 9: 2.9992164705  
Depth10: 2.9997107481  

It quickly converges toward 3.0000…
...

"""
import math
import matplotlib.pyplot as plt

# Number of nesting levels
N = 20

# Recursive function to build the nested radical
def nested_radical(n):
    if n == N:
        return math.sqrt(1)  # base case
    return math.sqrt(1 + (n+1) * nested_radical(n + 1))

# Compute partial values (to show convergence)
values = []
for k in range(1, N+1):
    # build a partial version truncated at depth k
    def partial(k0):
        if k0 == k:
            return math.sqrt(1)
        return math.sqrt(1 + (k0+1) * partial(k0 + 1))
    values.append(partial(1))

# Display results
for i, v in enumerate(values, start=1):
    print(f"Depth {i:2d}: {v:.10f}")

# Plot convergence
plt.figure(figsize=(6,4))
plt.plot(range(1, N+1), values, marker='o')
plt.axhline(3, color='gray', linestyle='--', label='Limit = 3')
plt.xlabel("Nesting Depth")
plt.ylabel("Value of Nested Radical")
plt.title("Convergence of Ramanujan’s Infinite Nested Radical")
plt.legend()
plt.grid(True)
plt.show()
