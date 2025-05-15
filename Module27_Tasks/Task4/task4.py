def caching(func):
    cached_data = dict()
    def cache_data(*args, **kwargs):
        if cached_data.get(args[1]):
            print('Cached info')
            return cached_data[args[1]]
        else:
            result = func(*args, **kwargs)
            cached_data[args[1]] = result
            return result
    return cache_data

class Task4:
    @caching
    def fib(self, number : int, sequence : list = [0, 1], n : int = 1):
        if number <= 2: 
            return 1
        if n != number:
            n += 1
            sequence.append(sequence[n - 1] + sequence[n - 2])
            return self.fib(number, sequence, n)
        else:
            n += 1
            return sequence[n - 1] + sequence[n - 2]