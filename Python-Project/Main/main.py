from parser_class import *

if __name__ == "__main__":
    parser_obj = Parser()
    parser_obj.parse_students()
    parser_obj.parse_answer_keys()
    parser_obj.parse_poll_reports()