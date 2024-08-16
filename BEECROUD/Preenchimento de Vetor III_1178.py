X = float(input()) 
N = [0.0] * 100  
N[0] = X  
for i in range(1, 100):
    N[i] = N[i - 1] / 2
for i in range(100):
    print(f"N[{i}] = {N[i]:.4f}")
