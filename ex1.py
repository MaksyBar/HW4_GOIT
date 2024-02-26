def total_salary(path):
     try:
         total_salary = 0
         num_developers = 0

         with open(path, 'r', encoding='utf-8') as file:
             for line in file:
                 name, salary_str = line.strip().split(',')
                 salary = int(salary_str.strip())
                 total_salary += salary
                 num_developers += 1

         average_salary = total_salary / num_developers
         return total_salary, average_salary

     except FileNotFoundError:
         print("Файл не знайдено!")
     except Exception as e:
         print(f"Сталася помилка: {str(e)}")


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")