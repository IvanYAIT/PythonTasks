from Module19_Tasks.Task4.Task4 import Task4

def test_convert_text_into_dict():
    text1 = "Здесь что"
    text2 = "aaaaaaaaaa"
    text3 = ""
    assert Task4.convert_text_into_dict(text1) == {"З" : 1, "д" : 1, "е" : 1, "с" : 1, "ь" : 1, " " : 1, "ч" : 1, "т" : 1, "о" : 1}
    assert Task4.convert_text_into_dict(text2) == {"a":10}
    assert Task4.convert_text_into_dict(text3) == {}

def test_inverse_dict():
    dict1 = {"З" : 1, "д" : 1, "е" : 1, "с" : 1, "ь" : 1, " " : 1, "ч" : 1, "т" : 1, "о" : 1}
    dict2 = {"a":10}
    dict3 = {}
    assert Task4.inverse_dict(dict1) == {1:["З", "д", "е", "с", "ь", " ", "ч", "т", "о"]}
    assert Task4.inverse_dict(dict2) == {10 : ["a"]}
    assert Task4.inverse_dict(dict3) == {}