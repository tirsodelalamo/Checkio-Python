
import unicodedata

def checkio(in_string):
    nfkd_form = unicodedata.normalize('NFKD', in_string)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])    

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
