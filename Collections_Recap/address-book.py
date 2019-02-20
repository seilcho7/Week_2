# Dictionaries
# a.k.a Hash, HashMap, HashTables, Map, Object

places = {
    'farm burger': '1234 piedmont, atlanta',
    'naan stop': '1553 piedmont, atlanta'
}

# what is the address of farm burger?
print(places['farm burger'])
# go get me the thing with 'farm burger'on the left hand side of the colon

friends = {
    'Europe': {
        'paris': ['frankie', 'grace'],
        'berlin': ['bobbie']
    },
    'Asia': ['my cousin', 'my other cousin', 'their cousin'],
    'US': {
        'angela': {
            'pets': {
                'oakley': {
                    'toys': ['everything', 'your stupid', 'strings']
                }
            }
        }
    }
}

print(friends['US'])
print(friends['Europe']['berlin'])
print(friends['Europe']['paris'][0])
print(friends['Europe']['paris'][1])

toys = friends['US']['angela']['pets']['oakley']['toys']

for item in toys:
    print("%s is one of oakley's fav toys" % (item,))