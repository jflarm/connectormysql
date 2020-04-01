#!/usr/bin/env python3.8

class Connection():
    """
    Clase Connection inicializa con un archivo de configuracion que contiene 
    los datos de: host, usuario, password, base de datos, unix_socket y puerto.
    Por defecto, se espera el archivo 'config.json'.
    """
    def __init__(self):

        import mysql.connector
        import json

        with open('config.json','r') as file:

            data = json.load(file)

            for option in data:
                options = {
                'host':data.get('host'),
                'user':data.get('user'),
                'password':data.get('password'),
                'database':data.get('database'),
                'unix_socket':data.get('unix_socket'),
                'port':data.get('port')
                }

            self.__connection = mysql.connector.connect(**options)

    def __getConnection(self):
        return self.__connection

    def singleQuery(self, sql):
        """
        El metodo singleQuery acepta como entrada un str con el 
        query SQL.
        """

        cursor = self.__getConnection().cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        return result 
