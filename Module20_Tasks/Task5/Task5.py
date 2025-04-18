class Task5:
    def tpl_sort(tpl):
        for num in tpl:
            if(type(num) is not int):
                return tpl
        return tuple(sorted(tpl))
            
    @classmethod
    def main(cls):
        tpl = (6, 3, -1, 8, 4, 10, -5)
        sorted_tpl = cls.tpl_sort(tpl)
        print(sorted_tpl)