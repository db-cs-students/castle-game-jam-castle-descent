"""
Title:Castle Descent
Creators:Adam and Eli
Description:
"""
#creating backgrounds
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffff
    fffffff1fffffffffffffffffffffffffffffff1ffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffff1ffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffccffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffcccfffffcffffffffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffcccccffffccffffffffffcccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffcccccccfffccffffffffffcccffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffcfccccfffcccfffffffffcccccfffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffff1ffffffffffffffffffcccccfffccccffffffffccccccfffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffcccccccfffccffffffffffccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffccccfccffcccfffffffccccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffccccccfffcccfffffffffccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffccfcccccffccccfffffffcccccfccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffccccccccccccffffffcccccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffcccccccccccccccccccffccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffcffffffffffcccccccccccccccccccccffccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffffffff
    ffffffffffffcccfffffffffffcccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffccffffffffffffffffff
    ffffffffffffccffffffffffccccccccccccccccccccccccccffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffccfffccffffffffffffffffff
    fffffffffffcccfffffffffccccccccccccccccccccccccccccfffffffffffffffffffffffffffffffffccfffffffffffffffffffffffffffffffffffffffffffffffffccffcccffffffffffffffffff
    ffffffffffcccccffffffcccccccccccccccccccccccccccccccffffffffffffffffffffffffffffffffccffffffffffffffffffffffffffffffffffffffffffffcfffccccfcccccffffffffffffffff
    fffffffffffcccfffffccccccccccccccccccccccccccccccccccffffffffffffffffffffffffffffffccccffffffffffffffffffffffffffffffffffffffffffcccffccccffccffffffffffffffffff
    ffffffffffffcccfffccccccccccccccccccccccccccccccccccccfffffffffffffffffffffffffffffccccffffcfffffffffffffffffffffffffffffffffffffcccfffccffccccccfffffffffffffff
    ffffffffffccccffcccccccccccccccccccccccccccccccccccccccfffffffffffffffffffffccffffffccfffffcffffffffffffffffffffffffffffffffffffccccfcccccccccfffffffffcffffffff
    fffffffffffcccccccccccccccccccccccccccccccccccccccccccccfffffffffffffffffffcccffffccccccfffccfffffffffffffffffffffffffffffffffffffcccfccccfffccffffffffcffffffff
    ffffffffffffcccccccccccccccccccccccccccccccccccccccccccccfffffffffffffffffccccfffffccccffffccffffffffffffffffffffffffffffffffffffcccffcccccffcffffffffccccffffff
    ffffffffffffccccccccccccccccccccccccccccccccccccccccccccccffffffffffffffffffcccffffcccccffcccfffffffffffffcffffffffffffffffffffcccccccccccccfcfffffffffcffffffff
    fffffffffffcccccccccccccccccccccccccccccccccccccccccccccccffffffffffffffffccccccfccccccccfccccfffffffffffccfffffffffffffffffffffcccccccccccccccccffffccccfffffff
    ffffffffffcccccccccccccccccccccccccccccccccccccccccccccccccfffff1ffffffffccccccfccccccccccfccffffffffffffcccfffffffffffffcfffffcccccffcccccccccccccfffcccfffffff
    ffffffffccccccccccccccccccccccccccccccccccccccccccccccccccccfffffffffffffffccccccffccccffffcccffffffffffcccccffffffffffffcffffccccccccccccccccccccccffcccccfffff
    fffffffccccccccccccccccccccccccccccccccccccccccccccccccccccccfffffffffffffccccccffccccccffcccffffffffffcccccccfffffffffffccfffffccccccccccccccccccccccccccffffff
    ffffffccccccccccccccccccccccccccccccccccccccccccccccccccccccccfffffffffffcccccccccccccccccccccccfffffffcfccccffffffffffffccffffccccccccccccccccccccccccccfffffff
    fffffccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfffffffffffffcccccccccccccccccccccccfffffcccccfffffffffffcccffffccccccccccccccccccccccccccfffffff
    fffcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfffffffffffccccccccccccccccccccccccccffcccccccfffffffffffcffffccccccccccccccccccccccccccccffffff
    ffcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccffffffffccccccccccccccccccccccccccccccfccccfcffffffffffccccffccccccccccccccccccccccccccccccffff
    fccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfffffcccccccccccccccccccccccccccccccccccccffffffffffffccffcccccccccccccccccccccccccccccccccff
    ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfffcccccccccccccccccccccccccccccccccccccccfffffffffccccccccccccccccccccccccccccccccccccccccc
    ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccffffffffffcccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccffffffffffccccccccccccccccccccccccccccccccccccccc
    ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfffffffccccccccccccccccccccccccccccccccccccccccc
    ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccffffcccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
"""))
game.splash("Press A to jump")
game.splash("You can climb walls by pressing A while against a wall")
game.splash("Press B to shoot arrows and slow the ghost")
#tilemaps
scene.set_tile_map(img("""
    ................................................
    ................................................
    7777...........................................6
    .............777...........................74477
    ......7777........7......................7..447.
    ...................7.............77.....7...44..
    ....................7.........7......77.....44..
    .............................7..............44..
    ...........777777.......777.................44..
    ..........77..........7.....................44..
    .........77........7........................44..
    ........77..................................44..
    .....77.....................................44..
    ....777.....................................44..
    777777744444444444444444444444444444444444444444
    777777744444444444444444444444444444444444444444
""")) #tilemap
scene.set_tile(7, img("""
    b d d d d d d d d d d d d d d c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    d b b b b b b b b b b b b b b c
    c c c c c c c c c c c c c c c a
"""), True) #ground
scene.set_tile(6, img("""
    c c c c c c c c c c c c c c c c
    c c c c c c c c c c c b b b b c
    c c c c c c c c c c c b b b b c
    c c c c c c c c c c c b b b b c
    c c c c c c b b b b c b b b b c
    c c c c c c b b b b c b b b b c
    c c c c c c b b b b c b b b b c
    c c c c c c b b b b c b b b b c
    c b b b b c b b b b c b b b b c
    c b b b b c b b b b c d d d d c
    c b b b b c b b b b b b b b b c
    c b b b b c d d d d b b b b b c
    c b b b b c b b b b b b b b b c
    c b b b b b b b b b b b b b b c
    c d d d d b b b b b b b b b b c
    c b b b b b b b b b b b b b b c
"""), True) #exit
scene.set_tile(2, img("""
    d 1 1 1 1 b 1 1 1 1 1 1 1 1 1 b
    1 d d d d d b d d d d d d d d b
    1 d d d d d b d d d d d d d d b
    1 d d d d d d b d d d d d d d b
    1 d d d d d d b d d d d d d d b
    1 d d d d d d b d d d d d d d b
    1 d d d d d d d b d d d d d d b
    1 d d d d d d d d b d d d d d b
    1 d d d d d d d d b d d d d d b
    1 d d d d d d d b 1 b b d d d b
    1 d d d d d d d b 1 d d b b d b
    1 d d d d d d b 1 d d d d d b b
    1 d d d d d b b 1 d d d d d d b
    1 d d d d d b 1 d d d d d d d b
    1 d d d d b b 1 d d d d d d d b
    b b b b b b b b b b b b b b b b
"""), True) #cracked wall
scene.set_tile(4, img("""
    5 4 4 5 5 4 4 4 4 2 2 2 4 4 4 4
    4 4 4 4 4 5 5 4 2 2 2 2 4 4 4 5
    4 2 2 2 4 4 5 4 2 2 4 4 5 5 5 5
    2 2 4 2 4 4 5 4 2 2 4 5 5 5 5 4
    2 2 2 2 4 4 5 4 2 2 4 4 5 5 4 4
    4 2 2 2 4 5 5 4 4 4 4 4 4 4 4 2
    2 2 2 4 4 5 5 5 4 4 2 2 2 2 2 2
    4 2 2 4 5 5 5 5 4 2 2 4 2 2 2 4
    5 4 4 4 4 4 4 5 5 4 2 2 2 4 4 4
    4 4 4 2 2 2 4 4 5 5 4 4 4 4 5 5
    4 2 2 2 2 2 2 2 4 5 5 5 5 5 5 5
    5 4 4 2 4 2 2 4 4 5 5 5 4 4 4 5
    5 5 4 2 2 2 4 4 4 5 5 4 2 2 2 4
    4 5 4 4 4 4 5 5 5 5 4 2 4 2 2 4
    4 5 5 5 5 5 5 4 4 4 2 4 2 4 2 4
    4 5 5 5 4 4 4 4 2 2 2 2 4 2 4 4
"""), True) #lava
scene.set_tile(5, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . 6 6 6 6 . . . . . .
    . . . . 6 6 6 5 5 6 6 6 . . . .
    . . . 7 7 7 7 6 6 6 6 6 6 . . .
    . . 6 7 7 7 7 8 8 8 1 1 6 6 . .
    . . 7 7 7 7 7 8 8 8 1 1 5 6 . .
    . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 .
    . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 .
    . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 .
    . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 .
    . . 6 8 7 7 8 6 6 6 6 6 8 6 . .
    . . 6 8 8 7 8 8 6 6 6 8 6 6 . .
    . . . 6 8 8 8 8 8 8 8 8 6 . . .
    . . . . 6 6 8 8 8 8 6 6 . . . .
    . . . . . . 6 6 6 6 . . . . . .
    . . . . . . . . . . . . . . . .
"""), True) #destroy ghost

#creating sprites
Knight = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . f f f f f f . . . . .
    . . . f f e e e e f 2 f . . . .
    . . f f e e e e f 2 2 2 f . . .
    . . f e e e f f e e e e f . . .
    . . f f f f e e 2 2 2 2 e f . .
    . . f e 2 2 2 f f f f e 2 f . .
    . f f f f f f f e e e f f f . .
    . f f e 4 4 e b f 4 4 e e f . .
    . f e e 4 d 4 1 f d d e f . . .
    . . f e e e e e d d d f . . . .
    . . . . f 4 d d e 4 e f . . . .
    . . . . f e d d e 2 2 f . . . .
    . . . f f f e e f 5 5 f f . . .
    . . . f f f f f f f f f f . . .
    . . . . f f . . . f f f . . . .
"""), SpriteKind.player)

tiles.place_on_tile(Knight, tiles.get_tile_location(3, 1))
Knight.ay = 175

scene.camera_follow_sprite(Knight)
#controls
controller.move_sprite(Knight, 75, 0)

def on_button_event_b_pressed(): #shoot arrow
    
    if controller.dx() > 0:
        arrow = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . b . . . .
            . . e e e e e e e e e b b . . .
            . . . . . . . . . . . b . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
        """), Knight, 100, 0)
    elif controller.dx() < 0:
        arrow = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . b . . . . . . . . . . .
        . . . b b e e e e e e e e e . .
        . . . . b . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """), Knight, -100, 0)
    else:
        arrow = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . b . . . . . . . . . . .
        . . . b b e e e e e e e e e . .
        . . . . b . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """), Knight, -100, 0)
controller.player1.on_button_event(ControllerButton.B, ControllerButtonEvent.PRESSED, on_button_event_b_pressed)

def on_jump(): #jump
    if Knight.is_hitting_tile(CollisionDirection.BOTTOM): 
        Knight.vy = -85
        music.play_melody("F5 C5", 500)
    elif Knight.is_hitting_tile(CollisionDirection.LEFT): #wall jump
        Knight.vy = -85
        music.play_melody("F5 C5", 500)
    elif Knight.is_hitting_tile(CollisionDirection.RIGHT):
        Knight.vy = -85 
        music.play_melody("F5 C5", 500)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_jump)

def on_update(): #turn sprite
    if Knight.vx > 0:
        Knight.set_image(img("""
            . . . . . . f f f f f f . . . .
            . . . . f f e e e e f 2 f . . .
            . . . f f e e e e f 2 2 2 f . .
            . . . f e e e f f e e e e f . .
            . . . f f f f e e 2 2 2 2 e f .
            . . . f e 2 2 2 f f f f e 2 f .
            . . f f f f f f f e e e f f f .
            . . f f e 4 4 e b f 4 4 e e f .
            . . f e e 4 d 4 1 f d d e f . .
            . . . f e e e 4 d d d d f . . .
            . . . . f f e e 4 4 4 e f . . .
            . . . . . 4 d d e 2 2 2 f . . .
            . . . . . e d d e 2 2 2 f . . .
            . . . . . f e e f 4 5 5 f . . .
            . . . . . . f f f f f f . . . .
            . . . . . . . f f f . . . . . .
        """))
    elif Knight.vx < 0:
        Knight.set_image(img("""
            . . . . f f f f f f . . . . . .
            . . . f 2 f e e e e f f . . . .
            . . f 2 2 2 f e e e e f f . . .
            . . f e e e e f f e e e f . . .
            . f e 2 2 2 2 e e f f f f . . .
            . f 2 e f f f f 2 2 2 e f . . .
            . f f f e e e f f f f f f f . .
            . f e e 4 4 f b e 4 4 e f f . .
            . . f e d d f 1 4 d 4 e e f . .
            . . . f d d d d 4 e e e f . . .
            . . . f e 4 4 4 e e f f . . . .
            . . . f 2 2 2 e d d 4 . . . . .
            . . . f 2 2 2 e d d e . . . . .
            . . . f 5 5 4 f e e f . . . . .
            . . . . f f f f f f . . . . . .
            . . . . . . f f f . . . . . . .
        """))
game.on_update(on_update)

#enemies
enemy = sprites.create(img("""
    ........................
    ........................
    ........................
    ........................
    ..........ffff..........
    ........ff1111ff........
    .......fb111111bf.......
    .......fd1111111f.......
    ......fdd1111111df......
    ......fddd111111df......
    ......fdddddd111df......
    ......fbddddbfd1df......
    ......fcbbbdcfddbf......
    .......fcbb11111f.......
    ........fffff1b1f.......
    ........fb111cfbf.......
    ........ffb1b1ff........
    ......f.fffbfbf.........
    ......ffffffff..........
    .......fffff............
    ........................
    ........................
    ........................
    ........................
"""), SpriteKind.enemy)

tiles.place_on_tile(enemy, tiles.get_tile_location(0, 1)) #put enemy at starting point

enemy.follow(Knight, 110, 20) #make enemy chase the player 

# info
info.set_life(3)
info.set_score(0)

def on_overlap(sprite, otherSprite): #hurt player when hitting enemy
    info.change_life_by(-1) #TODO try and make true invincibility frames
    enemy.set_flag(SpriteFlag.GHOST, True)
    enemy.vx = 0 
    enemy.vy = 0
    music.play_melody("E4 D4 C3", 300)

sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)
def on_overlap2(sprite, otherSprite): #stun enemy
    otherSprite.destroy()
    enemy.vx = -15
    enemy.vy = 0
    music.play_melody("F4 G4",1000)

sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_overlap2)
def on_life_zero(): #lose when dying
    game.over(False)
info.on_life_zero(on_life_zero)

def on_hit_tile(Knight): #reset on hit lava
    info.change_life_by(-1)

    tiles.place_on_tile(enemy, tiles.get_tile_location(0, 13))
    tiles.place_on_tile(Knight, tiles.get_tile_location(3, 13))

    enemy.vx = 0
    enemy.vy = 0
    music.play_melody("d3 c3", 120)
scene.on_hit_tile(SpriteKind.player, 4, on_hit_tile)

def on_hit_tile2(sprite): #win when hitting exit
    info.change_score_by(1)
    music.play_melody("e4 d4 e4 c4 e4 b4 a4", 350)

    if info.score() == 1:
        scene.set_tile_map(img("""
            ................................................
            ................................................
            ................................................
            ................................................
            ................................................
            ................................................
            ................................................
            ..................................777..........6
            .............................7777............777
            ...........................7.............777....
            ......................7777..........7777........
            ...................7..............7.............
            ..............7..7.............7777.............
            ..2..77777..7........7777..777..................
            7777777777......................................
            777777777744444444444444444444444444444444444444
        """))
    elif info.score() == 2:
        scene.set_tile_map(img("""
            ..............7.................................
            ..............7.................................
            ..............7.................................
            ..............7...777777777.....................
            ..............7...7.......7..7.......7.....7....
            ..............7...7.......7.........7...7......6
            ..............7...7.......7.......7..........7..
            ..............7...7.......7....7................
            ..............7...7.......7...7.................
            ..............2...7.......7.....................
            ..........777777777.......7777777777777777777777
            .........7......................................
            ........77......................................
            ......7.........................................
            7777777.........................................
            777777744444444444444444444444444444444444444444
        """))
        scene.set_tile(2, img("""
            d 1 1 1 1 b 1 1 1 1 1 1 1 1 1 b
            1 d d d d d b d d d d d d d d b
            1 d d d d d b d d d d d d d d b
            1 d d d d d d b d d d d d d d b
            1 d d d d d d b d d d d d d d b
            1 d d d d d d b d d d d d d d b
            1 d d d d d d d b d d d d d d b
            1 d d d d d d d d b d d d d d b
            1 d d d d d d d d b d d d d d b
            1 d d d d d d d b 1 b b d d d b
            1 d d d d d d d b 1 d d b b d b
            1 d d d d d d b 1 d d d d d b b
            1 d d d d d b b 1 d d d d d d b
            1 d d d d d b 1 d d d d d d d b
            1 d d d d b b 1 d d d d d d d b
            b b b b b b b b b b b b b b b b
        """), True)
    elif info.score() == 3:
        scene.set_tile_map(img("""
            ................................................
            ................................................
            ................................................
            ................................................
            ................................................
            ................................................
            ............77774.747474..74774.74...74....74..6
            ............7............7........74....74..4777
            ............7...................................
            ............7...................................
            ............7...................................
            ............7......................7............
            ............2...77774477..7.....7.....7.....7..6
            ..........7777......44.......7...........7....77
            77777777............44..........................
            444444444444444444444444444444444444444444444444
        """))
        scene.set_tile(2, img("""
        d 1 1 1 1 b 1 1 1 1 1 1 1 1 1 b
        1 d d d d d b d d d d d d d d b
        1 d d d d d b d d d d d d d d b
        1 d d d d d d b d d d d d d d b
        1 d d d d d d b d d d d d d d b
        1 d d d d d d b d d d d d d d b
        1 d d d d d d d b d d d d d d b
        1 d d d d d d d d b d d d d d b
        1 d d d d d d d d b d d d d d b
        1 d d d d d d d b 1 b b d d d b
        1 d d d d d d d b 1 d d b b d b
        1 d d d d d d b 1 d d d d d b b
        1 d d d d d b b 1 d d d d d d b
        1 d d d d d b 1 d d d d d d d b
        1 d d d d b b 1 d d d d d d d b
        b b b b b b b b b b b b b b b b
        """), True)
    elif info.score() == 4:
        scene.set_tile_map(img("""
            ................................................
            ................................................
            ................................................
            ................................................
            ................................................
            ................................................
            ................................................
            ................................................
            ................................................
            ........................7.......................
            ..................7..7.......77......7.........6
            ...............7..........7.......7......7....77
            .........7..7...............................7...
            ......7.........................................
            7777777.........................................
            444444444444444444444444444444444444444444444444
        """))
        scene.set_tile(2, img("""
        d 1 1 1 1 b 1 1 1 1 1 1 1 1 1 b
        1 d d d d d b d d d d d d d d b
        1 d d d d d b d d d d d d d d b
        1 d d d d d d b d d d d d d d b
        1 d d d d d d b d d d d d d d b
        1 d d d d d d b d d d d d d d b
        1 d d d d d d d b d d d d d d b
        1 d d d d d d d d b d d d d d b
        1 d d d d d d d d b d d d d d b
        1 d d d d d d d b 1 b b d d d b
        1 d d d d d d d b 1 d d b b d b
        1 d d d d d d b 1 d d d d d b b
        1 d d d d d b b 1 d d d d d d b
        1 d d d d d b 1 d d d d d d d b
        1 d d d d b b 1 d d d d d d d b
        b b b b b b b b b b b b b b b b
        """), True)
    elif info.score() == 5:
        scene.set_tile_map(img("""
            ................................................................................................
            ................................................................................................
            ................................................................................................
            ................................................................................................
            ................................................................................................
            ................................................................................................
            ..................................................................7.........7.......7.....7....7
            ...............................................................7..7..7...7......7...............
            ............................................................7.....7.....................7....7..
            .............7...........................................7........7.............................
            ................7..7.........7.......7................7...........7.............................
            ......777777..........7..7.......7.......7.........7..............7.............................
            .....7777777.................................7..7.................7.............................
            ....77777777......................................................7.............................
            777777777777......................................................7.............................
            7777777777777777777777777777777777777777777777777777777777777777777.............................
            7777777777777777777777777777777777777777777777777777777777777777777.............................
            7777777777777777777777777777777777777777777777777777777777777777777.............................
            7777777777777777777777777777777777777777777777777777777777777777777........3....................
            7777777777777777777777777777777777777777777777777777777777777777777.............................
            7777777777777777777777777777777777777777777777777777777777777777777.............................
            7777777777777777777777777777777777777777777777777777777777777777777.............................
            7777777777777777777777777777777777777777777777777777777777777777777.............................
            7777777777777777777777777777777777777777777777777777777777777777777.............................
            7777777777777777777777777777777777777777777777777777777777777777777.............................
            7777777777777777777777777777777777777777777777777777777777777777777.............................
            7777777777777777777777777777777777777777777777777777777777777777777.............................
            77777777777777777777777777777777777777777777777777777777777777777776.....7777.........7777.....5
            7777777777777777777777777777777777777777777777777777777777777777777777..........7777........7777
            777777777777777777777777777777777777777777777777777777777777777777744444444444444444444444444444
            777777777777777777777777777777777777777777777777777777777777777777744444444444444444444444444444
            777777777777777777777777777777777777777777777777777777777777777777744444444444444444444444444444
        """))
        scene.set_tile(2, img("""
            d 1 1 1 1 b 1 1 1 1 1 1 1 1 1 b
            1 d d d d d b d d d d d d d d b
            1 d d d d d b d d d d d d d d b
            1 d d d d d d b d d d d d d d b
            1 d d d d d d b d d d d d d d b
            1 d d d d d d b d d d d d d d b
            1 d d d d d d d b d d d d d d b
            1 d d d d d d d d b d d d d d b
            1 d d d d d d d d b d d d d d b
            1 d d d d d d d b 1 b b d d d b
            1 d d d d d d d b 1 d d b b d b
            1 d d d d d d b 1 d d d d d b b
            1 d d d d d b b 1 d d d d d d b
            1 d d d d d b 1 d d d d d d d b
            1 d d d d b b 1 d d d d d d d b
            b b b b b b b b b b b b b b b b
        """), True)
    elif info.score() == 6:
        game.over(True)
    tiles.place_on_tile(enemy, tiles.get_tile_location(0, 13))
    tiles.place_on_tile(Knight, tiles.get_tile_location(3, 13))

    enemy.vx = 0
    enemy.vy = 0
scene.on_hit_tile(SpriteKind.player, 6, on_hit_tile2)

def on_hit_tile3(enemy):
    enemy.set_flag(SpriteFlag.GHOST, True)
scene.on_hit_tile(SpriteKind.enemy, 7, on_hit_tile3)

def on_hit_tile4(sprite):
    scene.set_tile(2, img("""
        d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b
        1 d d d d d d b 1 d d d d d d b
        1 d d d d d d b 1 d d d d d d b
        1 d d d d d d b 1 d d d d d b b
        1 d d d d d d b 1 d d b b b c c
        1 d d d d d d d b b b c c c c c
        1 d d d d d d e b c 1 c c c c c
        b b b b b b e c c 1 d d c c c c
        c c c 1 c c c c c 1 d d c c c c
        c c c 1 1 c c c c c 1 d d c c c
        c c c 1 d d c c c c 1 d d c c c
        c c 1 d d d c c c c c d d d c c
        c c 1 d d d d c c c c d d b c c
        c c 1 d d d d d c c c b b c c c
        c c c b b b d d d b c c c c c c
        c c c c c c b b b c c c c c c c
    """), False)
    music.play_melody("B3 D3", 500)
scene.on_hit_tile(SpriteKind.projectile, 2, on_hit_tile4)

def on_hit_tile5(sprite):
    enemy.destroy()
    scene.set_tile(5, img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), False)
scene.on_hit_tile(SpriteKind.player, 5, on_hit_tile5)

def on_update_interval():
    enemy.set_flag(SpriteFlag.GHOST, False)
game.on_update_interval(750, on_update_interval)