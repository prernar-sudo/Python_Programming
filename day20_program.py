n = 5
fi, se = 0, 1

for _ in range(n):
    print(fi, end=' ')
    fi, se = se, fi + se
