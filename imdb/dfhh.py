import pandas as pd

chunksize = 1000  # Размер чанка
all_data ={}

for chunk in pd.read_csv('C:\Podkorytro01\PythonProjects\IMDBView\imdb_template.csv', chunksize=chunksize):
    # Обработка чанка (например, преобразование в словарь)
    print(chunk)
    # processed_chunk = chunk.to_dict(orient='records')
    # all_data.extend(processed_chunk)