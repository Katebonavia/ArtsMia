from database.DB_connect import DBConnect
from model.arco import Arco
from model.artObject import ArtObject


class DAO:

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor= conn.cursor(dictionary=True)

        result=[]
        query="""select * from objects o"""

        cursor.execute(query)

        for row in cursor:
            result.append(ArtObject(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllArchi(idMap): #passo un idMap che mi recupera gli oggetti dato l'id
        conn = DBConnect.get_connection()
        cursor= conn.cursor(dictionary=True)

        result=[]
        query="""select eo.object_id as o1, eo2.object_id as o2, count(*) as peso
                from exhibition_objects eo, exhibition_objects eo2 
                where eo2.exhibition_id = eo.exhibition_id 
                and eo2.object_id < eo.object_id
                group by eo.object_id, eo2.object_id
                order by peso desc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Arco(idMap[row["o1"]],idMap[row["o2"]],row["peso"]))#qui mi arriva un id di due oggetti e un peso che devo capire come gestire

        cursor.close()
        conn.close()

        return result