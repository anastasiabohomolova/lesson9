dictionary = {'salary': 100, 'name': 'Tom', 'factory': 'mixs'}
def func(a):
    text = open('text.txt', 'w')
    for key, value in a.items():
        text.write(f' {key} = {value}\n')
    text.close()
    return a

n = func(dictionary)
print(n)


