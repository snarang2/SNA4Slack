# config.py


class Config:
    APP_NAME = 'API_SNA4Slack'
    NODE_IP = '104.155.179.66'
    KEYSPACE_NAME = 'sna4slack_metrics'
    DB_USER = 'cassandra'
    DB_PASSWORD = 'LYN1bQNCds3T'
    DB_COLUMN_FAMILY = 'slack_archive_dev'
    MONGO_CLIENTURI = 'mongodb://aman2909:aman2909@ds161146.mlab.com:61146/sna4slack'
    #MONGO_CLIENTURI = 'mongodb://sna4slack:sna4slack@ds151461.mlab.com:51461/sna4slack'
    MONGO_DB_NAME = 'sna4slack'
