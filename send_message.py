import psycopg2
from twilio.rest import Client
from tabulate import tabulate 

# Configuración de la base de datos PostgreSQL
db_config = {
    'host': 'localhost',
    'port': '5432',
    'user': 'postgres',
    'password': 'postgres',
}

# Configuración de Twilio (necesitarás una cuenta de Twilio y un número de teléfono verificado)
twilio_config = {
    'account_sid': 'AC608cb760f5502e2a169e216f89beda92',
    'auth_token': '4b8638b15b988893fdd86a626fc95023',
    'from_whatsapp_number': 'whatsapp:+14155238886',  # Este es el número de Twilio, no lo cambies
    'to_whatsapp_number': 'whatsapp:+5493455532221'
}

def consultar_base_de_datos():
    # Conexión a la base de datos
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Ejecutar la consulta
    cursor.execute("SELECT * FROM bitcoin;")  # Modifica la consulta según tus necesidades
    resultados = cursor.fetchall()

    # Cerrar la conexión
    cursor.close()
    conn.close()

    return resultados

def enviar_whatsapp_mensaje(mensaje):
    # Conexión a Twilio
    client = Client(twilio_config['account_sid'], twilio_config['auth_token'])

    # Enviar mensaje de WhatsApp
    message = client.messages.create(
        
        from_= 'whatsapp:+14155238886',
        body=mensaje,
        to=twilio_config['to_whatsapp_number']
    )

    print(f"Mensaje enviado a {twilio_config['to_whatsapp_number']}: {message.sid}")

if __name__ == "__main__":
    # Consultar la base de datos
    resultados = consultar_base_de_datos()

    # Formatear los resultados como un mensaje
    mensaje = "Resultados de la consulta:\n"
    for resultado in resultados:
        mensaje += str(resultado) + "\n"
        
    tabla = tabulate(resultados, headers="firstrow", tablefmt="grid")

    print(tabla)
    # Enviar el mensaje de WhatsApp
    enviar_whatsapp_mensaje(tabla)
