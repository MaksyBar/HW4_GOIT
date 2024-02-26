def get_cats_info(path):
     

    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(',')
                cat_dict = {
                    'id': cat_id,
                    'name': cat_name,
                    'age': cat_age
                }
                cats_info.append(cat_dict)
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
    
    return cats_info


cats_info = get_cats_info("cats_file.txt")
print(cats_info)

