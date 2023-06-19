import calculator

def handle_request(params):
  sum = 0
  numbers = params['add']
  for n in numbers:
    sum += n
  return {
    'result': sum
  }
