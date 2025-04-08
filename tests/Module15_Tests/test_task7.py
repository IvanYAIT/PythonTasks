from Module15_Tasks.Task7.Task7 import Task7

def test_is_word_palindrome():
    assert Task7.is_word_palindrome("abccba") == True
    assert Task7.is_word_palindrome("123321") == True
    assert Task7.is_word_palindrome("мадам") == True
    assert Task7.is_word_palindrome("abbc") == False