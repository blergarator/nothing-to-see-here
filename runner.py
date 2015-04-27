import json
import requests
from requests.packages.urllib3.util import Retry
import requests.exceptions
from requests import adapters
from flask import Flask


import time
import sys
import re
from utils import dateFunc
import base64
import csv

sys.dont_write_bytecode = True

from peewee import (
    Model,
    CharField,
    OperationalError,
    TextField,
    BooleanField,
    fn
)

from playhouse.pool import PooledMySQLDatabase

# Collect db settings from untracked file
try:
    local_fd = open('settings.json')
    LOCAL = json.load(local_fd)
    local_fd.close()
except:
    LOCAL = {}

lazercat_db = PooledMySQLDatabase(
    LOCAL.get('schema_name'),
    host=LOCAL.get('host'),
    port=LOCAL.get('port'),
    user=LOCAL.get('user'),
    passwd=LOCAL.get('passwd'),
    max_connections=LOCAL.get('max_connections'),
    stale_timeout=LOCAL.get('stale_timeout'),
    threadlocals=LOCAL.get('threadlocals')
)


class MySQLModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = lazercat_db


class DataModel(MySQLModel):
    """ Set customer device info mysql model """
    common_name = CharField(default='')
    unique_id = CharField(default='', unique=True, primary_key=True)
    data_type = CharField(default='')
    lookup_alias = CharField(default='')
    array_data = TextField(default='')
    some_bool_field = BooleanField(default=False)
    lookup_mo_yr = CharField(default='')

class HtmlModel(MySQLModel):
    common_name = CharField(default='')
    html_data = CharField(default='')
    built = CharField(default='')

try:
    DataModel.create_table()
    HtmlModel.create_table()
except OperationalError:
    pass


class ApiInstance():
    def __init__(
            self,
            key=None,
            sec=None,
            endpoint=None,
            short_end=None,
            next_page=None,
            identifier=None
    ):
        # Init constants
        self.counter = 0
        self.key = key
        self.sec = sec
        self.endpoint = endpoint
        self.short_end = short_end
        self.next_page = next_page
        self.identifier = identifier
        self.a = None
        self.request = None
        self.batch_insert = []
        self.completed_list = []
        self.returned_calls = {}
        self.auth = str(('%s:%s' % (self.key, self.sec)).encode('base64')[:-1])
        self.headers = {
            'authorization': 'Basic %s' % self.auth,
            'Content-type': 'application/json',
            'Accept': '<some api accept data>'
        }

    def session_manager(self):
        """ Define session management values for re-use """

        if not self.request:
            self.request = requests.Session()
            self.a = requests.adapters.HTTPAdapter(
                pool_connections=10,
                pool_maxsize=10,
                max_retries=Retry(
                    total=8,
                    status_forcelist=[500, 503, 504, 401],
                    backoff_factor=1.3,
                    connect=8
                )
            )
            self.request.mount('https://', self.a)

    def api_caller(self, endpoint, passed_json=None):
        """ Make API calls off of pre-set class variables """

        passed_json = passed_json
        if passed_json:
            passed_json['next_page'] = None
        self.session_manager()
        response = self.request.get(
            endpoint,
            headers=self.headers
        )

        res_response = int(response.status_code)
        if not res_response == 200:
            print res_response
        unauth = [401, 400, 403]
        response = json.loads(response.text)
        if res_response in unauth:
            print res_response
            print response
            return False
            # time.sleep(1)
            # response = self.request.eget(
            #     endpoint,
            #     headers=self.headers
            # )
            # res_response = int(response.status_code)
            # if res_response in unauth:
            #     print 'Got a %s code' % res_response
            #     return False
            # else:
            #     if passed_json:
            #         for keys, vals in passed_json.iteritems():
            #             if isinstance(vals, list):
            #                 response[keys] = response[keys] + vals
        else:
            if passed_json:
                for keys, vals in passed_json.iteritems():
                    if isinstance(vals, list):
                        response[keys] = response[keys] + vals

        return response

    def get_data(self, endpoint):
        """ Instantiate API calls and append values when next_page found """

        if endpoint == 'turkeyshoot':
            # Not using pooling currently - may at some point
            # dev_div = maker()
            # response = []
            # pool = Pool(processes=16)  # !!! Set no higher than 16!!!
            # pool.map(dev_runner, dev_div, chunksize=1)
            print 'stuff'
        else:
            pass

    def build_dates(self):
        """ Build date values in ISO8601 format """

        self.monthdate = dateFunc.month_date(self.lm)
        self.daterange = dateFunc.daterange_date(self.lm)
        self.singledate = dateFunc.end_date(self.lm)

    def get_last_seen(self):
        """ Gets last seen values from database """

        three = dateFunc.end_date(24)
        print 'Three: %s' % three

        db = DataModel()

        for kittens in db.select().where(
            (
                (str(db.lookup_mo_yr) < str(three))
            )
        ):
            print kittens.channel,\
                kittens.lookup_mo_yr,\
                type(str(kittens.lookup_mo_yr)),\
                type(three)

    def make_html(self):
        """ Creates html out of stored data set """

        self.returned_calls[self.key] = {}
        single_end_date = dateFunc.single_date_hour("now")
        filename = "%s_out_%s_csvout.csv" % (
            self.key,
            str(single_end_date.format('YYYY-MM-DD-HH-mm'))
        )
        with open(filename, 'a') as outfile:
            print [x[1] for x in self.out_list]
            file_writer = csv.writer(
                outfile,
                delimiter=',',
                quoting=csv.QUOTE_MINIMAL
            )
            if len(self.out_list) >= 2:
                print self.out_list[1]
                self.out_list = reversed(
                    sorted(
                        self.out_list,
                        key=lambda target: target[16]
                    )
                )
            file_writer.writerow(self.push_eval_header())
            for x in self.out_list:
                file_writer.writerow(x)
        single_end_date = dateFunc.single_date_hour("now")

        jsonwriterz = "%s_out_%s_jsonout.json" % (
            keys,
            str(single_end_date.format('YYYY-MM-DD-HH-mm'))
        )
        with open(jsonwriterz, 'wb') as outfile:
            json.dump(
                self.returned_calls,
                outfile,
                sort_keys=True,
                indent=4
            )

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()