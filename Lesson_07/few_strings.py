# Create by Bender

"""
Дан текст состоящий из нескольких строк. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите последнее.
Задачу необходимо решить с использованием словаря.
"""

from re import sub

some_text = """
На небесах только и говорят, что о море. Как оно бесконечно прекрасно.
О закате, который они видели. О том, как солнце, погружаясь в волны, стало алым как кровь,
и почувствовали, что море впитало энергию светила в себя, и солнце было укрощено,
и огонь уже догорал в глубине. А ты? Что ты им скажешь?! Ведь ты ни разу не был на море.
Там наверху тебя окрестят лохом!...
"""

words = [val for i, val in enumerate(sub("[,.!?:;]", "", some_text.lower()).split())]
count_words = {i: words.count(i) for i in words}

print(sorted([(count, word) for word, count in count_words.items()]).pop()[1])
