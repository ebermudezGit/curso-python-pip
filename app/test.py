import csv


def read_csv(path):
  # Tu código aquí 👇
  with open(path, 'r') as csvfile:
    total = sum([int(row[1]) for row in csv.reader(csvfile, delimiter=',')])
  return total


response = read_csv('./app/data_test.csv')
print(response)
