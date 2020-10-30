import matplotlib.pyplot as plt

def scatter(acc, color):
    marker = ([ (-1, 0), (1, 0), (1, acc.nblks), (-1, acc.nblks) ], 0)
    plt.scatter(acc.timestamp, acc.lba, marker = marker, c = color)

def plot(ta, args):
    for acc in ta.accesses:
        if acc.is_read:
            if not args.writeonly:
                scatter(acc, 'red')
        else:
            if not args.readonly:
                scatter(acc, 'blue')

    plt.show()
