def nb_year(p0, percent, aug, p):
    totPop = p0
    years = 0
    
    while totPop < p:
        totPop = totPop+totPop*(percent/100)+aug
        years += 1
    
    return years


print(nb_year(1500, 5, 100, 5000) == 15)
print(nb_year(1500000, 2.5, 10000, 2000000) == 10)
print(nb_year(1500000, 0.25, 1000, 2000000) == 94)