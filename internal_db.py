import psycopg2
import traceback
import config as cfg

class InternalDB:
    def initial_connection_to_database(self):

        # Try to connect
        try:
            psycopg2.connect(cfg.db_connect)
        except:
            print('failed to connect to DB')

    def initialize_import_to_database(self, potential_pidors):
        # Testing set
        potential_pidors_set = {
            '142715592468594694': {
                'name': 'naumchas',
                'display_name': 'naumchas#6637',
                'bot': False,
                'created_at': '2016-01-29 19:40:48.772000'
            },
            '143022070429646848': {
                'name': 'BizkitCake',
                'display_name': 'BizkitCake#8836',
                'bot': False,
                'created_at': '2016-01-30 15:58:38.812000'
            }}

        try:
            conn = psycopg2.connect(cfg.db_connect)
            conn.autocommit = True
        except:
            print("Fail to connect to DB")
        cur = conn.cursor()
        try:
            cur.execute("""SELECT pidor_id FROM pidors""")
            act_pids = list()
            # Obtaining data from select in list
            for i in cur.fetchall():
                act_pids.append(i[0])
        except:
            print('fail to insert')
            # Verifying data not in database then add DB
        for pid in potential_pidors:
            if int(pid) not in act_pids:
                try:
                    cur.execute("""INSERT into pidors(pidor_id, pidor_name) values({}, '{}')""".format(pid, potential_pidors[pid]['display_name']))
                except:
                    print('Failed to insert new data')
        return True

    def increase_being_pidor_value(self, pid):
        try:
            conn = psycopg2.connect(cfg.db_connect)
            conn.autocommit = True
        except:
            print("Failed to connect to DB")
        cur = conn.cursor()
        try:
            cur.execute("""SELECT being_pidor FROM pidors WHERE pidor_id = {}""".format(int(pid)))
            counter = cur.fetchone()[0]
        except:
            print("Failed to get being_pidor data")
        try:
            cur.execute("""UPDATE pidors set being_pidor = {} where pidor_id = {}""".format(counter + 1, pid))
        except:
            print("Failed to update being_pidor")

    def update_activity_table(self, pid):
        try:
            conn = psycopg2.connect(cfg.db_connect)
            conn.autocommit = True
        except:
            print("Failed to connect to DB")
        cur = conn.cursor()
        try:
            cur.execute("""UPDATE activity set last_activity = now(), last_pidor_id = {}""".format(int(pid)))
        except:
            print("Failed to update activity")

    # TODO extract condition to this function
    def check_if_user_is_in_database(member_id):
        pass

    def update_user_name_if_changed(member_id, member_name):
        pass