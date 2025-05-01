from database.DB_connect import DBConnect
from model.Airport import Airport
from model.Flight import Flight


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllFlights():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM flights"""

        cursor.execute(query)

        for row in cursor:
            result.append(
                Flight(row["ID"], row["AIRLINE_ID"], row["FLIGHT_NUMBER"], row["TAIL_NUMBER"], row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["SCHEDULED_DEPARTURE_DATE"], row["DEPARTURE_DELAY"], row["ELAPSED_TIME"],row["DISTANCE"], row["ARRIVAL_DATE"], row["ARRIVAL_DELAY"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAirport():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM airports"""

        cursor.execute(query)

        for row in cursor:
            result.append(
                Airport(row["ID"], row["IATA_CODE"], row["AIRPORT"], row["CITY"], row["STATE"], row["COUNTRY"], row["LATITUDE"], row["LONGITUDE"], row["TIMEZONE_OFFSET"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesPesati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT x.ORIGIN_AIRPORT_ID, x.DESTINATION_AIRPORT_ID,SUM(x.DISTANCE)/COUNT(x.ID) as mediaDistanze
                FROM extflightdelays.flights x
                GROUP BY x.ORIGIN_AIRPORT_ID, x.DESTINATION_AIRPORT_ID
                ORDER BY mediaDistanze DESC;;
                   """

        cursor.execute(query)

        for row in cursor:
            result.append((row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["mediaDistanze"]))
        cursor.close()
        conn.close()
        return result
