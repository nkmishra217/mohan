m = input()
print(''.join([ m[h:h+2][::-1] for h in range(0, len(m), 2) ]))
