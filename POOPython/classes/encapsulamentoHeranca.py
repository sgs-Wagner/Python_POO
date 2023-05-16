class DatabaseConn:

    def __init__(self):
        self.__database = 'Postgres'
        self._conn = '//connection_string'
        self.user = 'wagner'

    def get_database(self):
        print(self.__database)

    def _testing_connection(self):
        print('connection ok')

class Repository(DatabaseConn):

    def __init__(self):
        super().__init__()

    def select(self):
        self._testing_connection()
        print('connection to {}'.format(self._conn))
        print('select * from table')
        print(self.user)
    # na pratica _ é uma convencão, só __ que python respeita


repo = Repository()
repo.select()