
def is_majority(items: list) -> bool:
    # your code here
    isTrue=0
    isFalse=0
    
    for i in items:
        if i is True:
            isTrue+=1
        else:
            isFalse+=1
            
    if isTrue>isFalse:
        return True
    elif isFalse>isTrue:
        return False
    elif isTrue==isFalse:
        return False
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
