from Module21_Tasks.Task3.Task3 import Task3

def test_deepcopy():
    data = {
    	'html': {
    		'head': {
    			'title': 'Куплю/продам телефон недорого'
    		},
    		'body': {
    			'h2': 'У нас самая низкая цена на телефон',
    			'div': 'Купить',
    			'p': 'продать'
    		}
    	}
    }
    task = Task3()
    copied_data = task.deepcopy(data, "iphone")
    assert copied_data == {'html': {'head': {'title': 'Куплю/продам iphone недорого'}, 'body': {'h2': 'У нас самая низкая цена на iphone', 'div': 'Купить', 'p': 'продать'}}}
    assert id(data) != id(copied_data)