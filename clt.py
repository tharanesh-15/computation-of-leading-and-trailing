grammar = {
    'E': ['E+T', 'T'],
    'T': ['T*F', 'F'],
    'F': ['(E)', 'id']
}

non_terminals = list(grammar.keys())

LEADING = {nt: set() for nt in non_terminals}
TRAILING = {nt: set() for nt in non_terminals}


def is_terminal(symbol):
    return not symbol.isupper()



def compute_leading():
    changed = True
    while changed:
        changed = False
        for head in grammar:
            for production in grammar[head]:
                symbols = list(production)

               
                if is_terminal(symbols[0]):
                    if symbols[0] not in LEADING[head]:
                        LEADING[head].add(symbols[0])
                        changed = True

                
                else:
                    for sym in LEADING[symbols[0]]:
                        if sym not in LEADING[head]:
                            LEADING[head].add(sym)
                            changed = True



def compute_trailing():
    changed = True
    while changed:
        changed = False
        for head in grammar:
            for production in grammar[head]:
                symbols = list(production)

               
                if is_terminal(symbols[-1]):
                    if symbols[-1] not in TRAILING[head]:
                        TRAILING[head].add(symbols[-1])
                        changed = True

              
                else:
                    for sym in TRAILING[symbols[-1]]:
                        if sym not in TRAILING[head]:
                            TRAILING[head].add(sym)
                            changed = True


compute_leading()
compute_trailing()


print("LEADING sets:")
for nt in LEADING:
    print(f"{nt} : {LEADING[nt]}")

print("\nTRAILING sets:")
for nt in TRAILING:
    print(f"{nt} : {TRAILING[nt]}")