if __name__ == '__main__':
  lis=[]
  for _ in range(int(input())):
      command, *value = input().split()
      if command == 'print':
          print(lis)
      else:
          getattr(lis,command)(*(map(int, value)))