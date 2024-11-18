queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
  ]



def main(queries: list[str]) -> None:

  queries_map = {}

  for query in queries:
    words = query.split()
    if len(words) in queries_map:
      queries_map[len(words)] += 1
    else:
      queries_map[len(words)] = 1

  for number_of_words, count in queries_map.items():
    print(f"Поисковых запросов, содержащих {number_of_words} слов(а): {format_percent(count, len(queries))}")



def format_percent(count: int, total_count: int) -> str:
  return f"{ round(count / total_count * 100, 2) }%"



main(queries)
