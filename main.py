def get_prime():
    '''
    Generator function yields next Prime number with every iteration
    '''
    p = 1

    while True:  # inifinite loop for generating next prime number
        p = p+1  # we start with the natural number p = 2
        i=2      
        while i < p:    # iterate over all divisors of p
            if p%i==0:  # if i is a divisor, then p is not a prime, we 
                p = p+1 # jump to check the next natural number
                i = 2   # roll i back to 2 for fresh start for next natural number
            else:
                i = i+1 # if i is not a divisor, increment and check again

        # if no divisors were found and we reached i = p, then p is prime and yield it
        yield p   

def find_largest_prime(n):
    '''
    (int)->int,str

    function takes natural number n>1 and returns the biggest prime divisor of it.
    

    '''

    if isinstance(n, int) and n>1:
        
        prime_list = []          # will contain all prime divisors
        
        next_prime = get_prime() # generator function for primes

        p = next(next_prime)     # get the first prime
        while p <= n: 
            
            if n%p==0:          # if current prime is a divisor for n, append it
                prime_list.append(p)
                n = n/p 
            else:    
                p = next(next_prime) # if not, get the next prime
        if len(prime_list)!=0:
            return prime_list[-1] # if we have at least one prime divisor, return the biggest
        else:
            return "no prime divisors"
    else:
        raise ValueError
