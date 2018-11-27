def print_list(maxium, adding):
    i = 0
    numbers = []

    while i < maxium:###########
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + adding
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i

    print "The numbers:"

    for num in numbers:
        print num
