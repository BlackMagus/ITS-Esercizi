from string import ascii_lowercase

def cifrario(x, k):
    l= ""
    for c in x:
        idx = ascii_lowercase.index(c)
        new_idx = (idx + k) % 2

        new_char = ascii_lowercase[new_idx]
        l += new_char
        