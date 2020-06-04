def readNumber(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    keta = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * keta
      keta /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index


def readPlus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1

def readMinus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1

def readMul(line, index):
  token = {'type': 'MUL'}
  return token, index + 1

def readDiv(line, index):
  token = {'type': 'DIV'}
  return token, index + 1

def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    elif line[index] == '+':
      (token, index) = readPlus(line, index)
    elif line[index] == '-':
      (token, index) = readMinus(line, index)
    elif line[index] == '*':
      (token, index) = readMul(line, index)
    elif line[index] == '/':
      (token, index) = readDiv(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens

#calculate * / until you reach + - or the end of token.
#returns calculated value and the index of +- or the last index of token.
def calcMulDiv(tokens, index):
  ans = 1
  i = index
  tokens[i-1]={'type': 'MUL'} # change token[i-1] to a dummy '*' token
  while i < len(tokens):
    if tokens[i]['type'] == 'NUMBER':
      if tokens[i - 1]['type'] == 'MUL':
        ans *= tokens[i]['number']
      elif tokens[i - 1]['type'] == 'DIV':
        ans /= tokens[i]['number']
      elif tokens[i - 1]['type'] == 'PLUS' or 'MINUS':
        return ans, i-1
      else:
        print('Invalid syntax')
        exit(1)
    i += 1
  return ans, i-1

def evaluate(tokens):
  answer = 0
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 1
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'PLUS':
        ans, index = calcMulDiv(tokens, index)
        answer += ans
      elif tokens[index - 1]['type'] == 'MINUS':
        ans, index = calcMulDiv(tokens, index)
        answer -= ans
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
  return answer


def test(line):
  tokens = tokenize(line)
  actualAnswer = evaluate(tokens)
  expectedAnswer = eval(line)
  if abs(actualAnswer - expectedAnswer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expectedAnswer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
  print("==== Test started! ====")
  test("1+2")
  test("1.0+2.1-3")
  test("-1+2")
  test("1*3-3/6")
  test("2.0*3.5-3/6")
  test("2.0*3.5-3/6.0")
  print("==== Test finished! ====\n")

runTest()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)