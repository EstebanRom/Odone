# Poseo un poco de dudas con respecto al desarrollo de este punto ya que no se si desean
# que realice la consulta como si no estubiera el servidor activo y ejecutar la busqueda
# directamente desde python o realizar la consulta de la base de datos desde python, por
# desarrollo mas comercial desde mi punto de vista realice el segundo, aunque es mucho
# mas simple, dado el caso estaria realizando la correccion de ser posible

import sqlite3

conn = sqlite3.connect('Base.db')

cursor = conn.cursor()
query = """
SELECT order_id, amount_total, customer_name
FROM orders
WHERE amount_total > 1000;
"""

cursor.execute(query)
orders = cursor.fetchall()

for order in orders:
    print(order)

conn.close()
