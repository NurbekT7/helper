class NumberQuery:
    def __init__(self, data):
        self.data = data

    def filter_even(self):
        return NumberQuery([x for x in self.data if x % 2 == 0])

    def multiply(self, factor):
        return NumberQuery([x * factor for x in self.data])

    def greater_than(self, threshold):
        return NumberQuery([x for x in self.data if x > threshold])

    def result(self):
        return self.data


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

''' это как бы аналог Model.objects.filter("field"="value").values_list("price", flat_true).distinct ну короче chain функции. Велус Лист не внутри Фильтр. просто Model.objects возврашает QuerySet, после фильтра тоже возвращает QuerySet, и так далее'''
result = NumberQuery(data).filter_even().multiply(3).greater_than(15).result()

print(result)
