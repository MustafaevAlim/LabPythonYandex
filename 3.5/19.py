import string

alf_low = string.ascii_lowercase
alf_up = string.ascii_uppercase
shift = int(input())
ans = ''
with open('public.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        s = ''
        for j in i:
            if j in alf_low:
                if alf_low.index(j) + shift < len(alf_low):
                    s += alf_low[alf_low.index(j) + shift]
                else:
                    s += alf_low[(alf_low.index(j) + shift) - len(alf_low)]
            elif j in alf_up:
                if alf_up.index(j) + shift < len(alf_up):
                    s += alf_up[alf_up.index(j) + shift]
                else:
                    s += alf_up[(alf_up.index(j) + shift) - len(alf_up)]
            else:
                s += j
        ans += s


with open('private.txt', 'w', encoding='utf-8') as f:
    f.write(ans)
    
