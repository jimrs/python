def hasGoodFormat(bn):
    if "/" in bn:
        bnList = bn.split("/")
        left = bnList[0]
        right = bnList[1]

        if len(left) == 6 and left.isnumeric():
            if len(right) == 4 and right.isnumeric():
                return True
        
    return False
