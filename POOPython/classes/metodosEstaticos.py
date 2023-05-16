
class Error:

    @staticmethod
    def error_500():
        return 'Internal Server Error'

    @staticmethod
    def error_404():
        return 'Not found'