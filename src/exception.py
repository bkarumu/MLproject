# refer to python exception documentation
# create funtion to define how  an error should look like 
# in my files
import sys

def error_message_detail(error, error_detail:sys):
    _,_,error_detail.exc_info()
    file_name =exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb.lineno,str(error)
        return error_message
        )
    
# created own custom exception class using exception documentation
class CustomException(Exception):
    def__init__(self, error_message, error_detail:sys):
    super.__init__(error_message)
    self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def__str__(self):
    return self.error_message

