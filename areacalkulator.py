print('cirkle/ellipse area calculator version 0.3.0 by leadattic_')
what = input('cirkle / ellipse / rectangle: ')

if what == 'cirkle':
    radie = input('radie: ')
    print(float(radie) * float(radie) * float(3.14159265359))
    input('press anything to leave')
elif what == 'ellipse':
    majoraxis = input('half of the major axis: ')
    minoraxis = input('half of the minor axis: ')
    print(float(majoraxis) * float(minoraxis) * float(3.14159265359))
    input('press anything to leave')
else:
    longside = input('long side: ')
    shortside = input('short side: ')
    print(float(longside) * float(shortside))
    input('press anything to leave')
