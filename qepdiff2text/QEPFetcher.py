import psycopg2


class QEPFetcher:
    def __init__(self, host, dbname, user, password, port=5432):
        self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
        self.cur = self.conn.cursor()

    def fetch_json(self, query):
        try:
            self.cur.execute('explain (format json) ' + query)
            analyze_fetched = self.cur.fetchall()[0][0][0]['Plan']
            self.conn.rollback()
            return analyze_fetched
        except:
            pass
        self.conn.rollback()
        return None
