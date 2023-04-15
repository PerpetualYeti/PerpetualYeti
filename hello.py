from datetime import datetime

def main():
  name = str('Ali')
  now = datetime.now()
  
  print(f'Hello, my name is {name}')
  print(f'It is currently {now.strftime("%H:%M:%S")}')


if __name__ == "__main__":
  main()
