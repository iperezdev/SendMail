import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constantes para la conexión de correo
GMAIL_USER = "test@gmail.com"  # Cambia esto por tu correo de Gmail
GMAIL_PASSWORD = "contraseña_aplicación"  # Usar una contraseña de aplicación de Google ya que Gmail no permite el inicio de sesión con contraseñas normales en aplicaciones menos seguras
RECIPIENT_EMAIL = "example@gmail.com"  # Cambia esto por el correo del destinatario
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# URL para la solicitud GET
URL = "https://jsonplaceholder.typicode.com/todos/1"

def get_json_title():
    """Realiza una petición GET y obtiene el título del JSON"""
    response = requests.get(URL)
    
    # Verifica si la petición fue exitosa
    if response.status_code == 200:
        data = response.json()
        return data.get("title", "No se encontró título")
    else:
        return f"Error al obtener datos: {response.status_code}"

def send_email(subject, body):
    """Envía un correo electrónico con el asunto y cuerpo especificados"""
    try:
        # Configurar el mensaje
        message = MIMEMultipart()
        message["From"] = GMAIL_USER
        message["To"] = RECIPIENT_EMAIL
        message["Subject"] = subject
        
        # Añadir el cuerpo del mensaje
        message.attach(MIMEText(body, "plain"))
        
        # Conectar al servidor SMTP de Gmail
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.send_message(message)
        
        return True, "Correo enviado exitosamente"
    except Exception as e:
        return False, f"Error al enviar el correo: {str(e)}"

def main():
    # Obtiene el título del TODO
    json_title = get_json_title()
    print(f"Título obtenido: {json_title}")
    
    # Enviar el correo con el título obtenido
    subject = "Información del JSON"
    body = f"El título del JSON es: {json_title}"
    
    success, message = send_email(subject, body)
    print(message)

if __name__ == "__main__":
    main()