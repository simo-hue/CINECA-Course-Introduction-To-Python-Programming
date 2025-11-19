def trapezoidal_integration(a, b, tol, f, maxsteps=2**23):
    # initialization
    intervals = 1
    acc = (f(a) + f(b))*0.5
    dx = (b - a) / intervals
    estimate = acc * dx
    prev_estimate = estimate + 2*tol 
    convergence = False
    steps = 1
    
    # iterative estimate
    while abs(estimate - prev_estimate) > tol:
        print("Current estimate using ", intervals, " intervals with dx =", dx, " is ", estimate)
        
        prev_estimate = estimate
        intervals *= 2 ; dx *= 0.5
        
        for i in range(1, steps + 1, 2): # only contributions from new points
            x = a + i*dx ; acc += f(x)
            
        estimate = acc*dx
        steps = steps + 1
        
        if steps > maxsteps: 
            break
    else:
        convergence=True
    return estimate, convergence

def integrand(x):
    return x**2

integral, success = trapezoidal_integration(a=-1.0, b=2.0, tol=1.e-4, f=integrand)
print("integral, success: ", integral, success)