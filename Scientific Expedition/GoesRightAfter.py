
def goes_after(word: str, first: str, second: str) -> bool:
    # your code here
    ind1 = word.find(first);
    ind2 = word.find(second);
    
    if (first in word) and (second in word):
        if ind2==ind1+1:
            return True
        else:
            return False
    else:
        return False



if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'w', 'r') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
