def find_message(text: str) -> str:
    """Find a secret message"""
    total=""
    
    for i in text:
        if i.isupper(): #.isupper() cheks if i is TRUE (i is Upper Letter) or FALSE
            total=total+i
    return total
        

if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")