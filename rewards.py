
import mysql.connector
import streamlit as st
import pandas as pd
import numpy as np
import MySQLdb
import sshtunnel

sshtunnel.SSH_TIMEOUT = 10.0
sshtunnel.TUNNEL_TIMEOUT = 10.0

with sshtunnel.SSHTunnelForwarder(
    (st.secrets["sshHost"], 22),
    ssh_username=st.secrets["sshUser"], ssh_password=st.secrets["sshPass"],
    remote_bind_address=(st.secrets["remoteH"], 3306)
) as tunnel:
    connection = MySQLdb.connect(
        user=st.secrets["dbUser"],
        passwd=st.secrets["dbPass"],
        host='127.0.0.1', port=tunnel.local_bind_port,
        db=st.secrets["dbName"],
    )
    # Do stuff
    connection.close()

mydb = mysql.connector.connect(
    host=st.secrets["host"], 
    user=st.secrets["user"], 
    password=st.secrets["password"], 
    database=st.secrets["database"]
    )
# create an object to show databases
c = mydb.cursor()

def get_code():
    d = []
    c.execute('SELECT IATA, CITY, COUNTRY FROM airportcity')
    data = c.fetchall()
    for da in data:
        da1 = f'{da[0]} {da[1]} {da[2]}'
        d.append(da1)
    return d
st.write(get_code())