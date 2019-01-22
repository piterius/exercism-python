def recite(start, stop):
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh',
            'twelfth']
    gifts = ['a Partridge in a Pear Tree.',
             'two Turtle Doves, and ',
             'three French Hens, ',
             'four Calling Birds, ',
             'five Gold Rings, ',
             'six Geese-a-Laying, ',
             'seven Swans-a-Swimming, ',
             'eight Maids-a-Milking, ',
             'nine Ladies Dancing, ',
             'ten Lords-a-Leaping, ',
             'eleven Pipers Piping, ',
             'twelve Drummers Drumming, ']
    return ["On the {0} day of Christmas my true love gave to me, {1}".format
            (days[j], "".join(gifts[i] for i in range(j, -1, -1))) for j in range(start-1, stop, 1)]
