# #q5.
# def file_in(input_name, output_file):
#     def decorator(funk):
#         def warepped(data):
#     with open(input_name, 'w+') as f :
#      f.write(str(data))            
#      result = funk(data)
#     with open(output_file, 'w+') as f:
#        f.write(str(result))
#        return result
#     return warepped
#     return 
# @file_in(inout_file = 'input.txt', output_file= 'output,txt')
# def procsses_data(data):
#    return data


def file_in(input_name, output_file):
 def decorator(funk):
  def warepped(data):
   with open(input_name, 'w+') as f:
    f.write(str(data))            
   result = funk(data)
   with open(output_file, 'w+') as f:
    f.write(str(result))
   return result
  return warepped
 return decorator

@file_in(input_name='input.txt', output_file='output.txt')
def procsses_data(data):
 return data


       