from Module21_Tasks.Task2.Task2 import Task2

def test_get_value_by_key():
    site = {
    	'html': {
    		'head': {
    			'title': 'Мой сайт'
    		},
    		'body': {
    			'h2': 'Здесь будет мой заголовок',
    			'div': 'Тут, наверное, какой-то блок',
    			'p': 'А вот здесь новый абзац',
                'data' : {'data' : 'data'}
    		}
    	}
    }
    task = Task2()
    assert task.get_value_by_key(site, 'head', -1) == {'title': 'Мой сайт'}
    assert task.get_value_by_key(site, 'head', 1) == None
    assert task.get_value_by_key(site, 'bd', -1) == None