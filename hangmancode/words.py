words=["shehzin","mad","scientist","gone","she","next","one","right","get","over","it","well","all","for","best","face","ice","deer","house","apple"]
def wordstarerr(hang,ba):
    import time
    from os import system
    p1='  *  '
    p2='*****'
    p3='*   *'
    p4=' * * '
    p5=' *** '
    p6='  ***'
    p7='***  '
    p8=' *   '
    p9='   * '
    p10='*    '
    p11='    *'
    p12='**** '
    spac='  '
    space={0:'  ',1:'  ',2:'  ',3:'  ',4:'  '}
    val=['','','','','','']
    s={0:p6,1:p8,2:p2,3:p9,4:p7}
    a={0:p1,1:p4,2:p2,3:p3,4:p3}
    h={0:p3,1:p3,2:p2,3:p3,4:p3}
    e={0:p2,1:p10,2:p2,3:p10,4:p2}
    z={0:p2,1:p9,2:p1,3:p8,4:p2}
    i={0:p2,1:p1,2:p1,3:p1,4:p2}
    n={0:'*   *',1:'**  *',2:'* * *',3:'*  **',4:'*   *'}
    b={0:'**** ',1:p3,2:p2,3:p3,4:'**** '}
    c={0:'  ***',1:' *   ',2:'*    ',3:' *   ',4:'  ***'}
    d={0:'**** ',1:p3,2:p3,3:p3,4:'**** '}
    f={0:p2,1:p10,2:p2,3:p10,4:p10}
    g={0:p2,1:p10,2:'* ***',3:p3,4:p2}
    j={0:p2,1:p11,2:p11,3:p3,4:p5}
    k={0:p3,1:'*  * ',2:'**   ',3:'*  * ',4:p3}
    l={0:p10,1:p10,2:p10,3:p10,4:p2}
    m={0:p3,1:'** **',2:'* * *',3:p3,4:p3}
    o={0:p5,1:p3,2:p3,3:p3,4:p5}
    p={0:p12,1:p3,2:p12,3:p10,4:p10}
    q={0:p5,1:'*   *',2:'* * *',3:'*  * ',4:'  *  *'}
    r={0:p2,1:p3,2:p2,3:'* *  ',4:p3}
    t={0:p2,1:p1,2:p1,3:p1,4:p1}
    u={0:p3,1:p3,2:p3,3:p3,4:p5}
    v={0:p3,1:p3,2:p3,3:p4,4:p1}
    w={0:p3,1:p3,2:'* * *',3:'** **',4:p3}
    x={0:p3,1:p4,2:p1,3:p4,4:p3}
    y={0:p3,1:p4,2:p1,3:p1,4:p1}

    #LOGIC
    tank=[]
    inp=hang
    inp=inp.lower()
    for var in inp:
        if var==' ':
            tank.append(space)
        else:
            tank.append(locals()[var])

    for i in range(0,5):
        for j in tank:
            val[i]=val[i]+spac+j[i]

    for i in val:
        print(i)
        time.sleep(ba)