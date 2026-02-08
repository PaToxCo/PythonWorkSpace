from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich import box
import pyfiglet
import time

console = Console()
usuarios_db = [
    {
        "id": 1,
        "name": "Rodrigo",
        "email": "admin@datux.com",
        "password": "123",
        "type_user": "admin",
        "status": True
    },
    {
        "id": 2,
        "name": "Jimena",
        "email": "jimena@datux.com",
        "password": "123",
        "type_user": "ventas",
        "status": True
    }
]

propiedadesDb = []
class EmailService:
    def send_email(self, destinatario, asunto, mensaje):
        console.print(f"\n[bold green] [SIMULACION] Enviando correo a {destinatario} [/bold green]")
        console.print(f"[dim]Asunto: {asunto}[/dim]")
        console.print("[bold green] Correo enviado exitosamente.[/bold green]")
emailService = EmailService()

def login_mock(email, password):
    for user in usuarios_db:
        if user["email"] == email and user["password"] == password:
            return user
    return None

def registrar_propiedad():
    console.clear()
    console.print(Panel("[bold cyan]REGISTRO DE NUEVA PROPIEDAD[/bold cyan]", expand=False))

    nombre = Prompt.ask("Nombre de la Propiedad")
    direccion = Prompt.ask("Dirección")
    precio = Prompt.ask("Precio (USD)")
    tipo = Prompt.ask("Tipo", choices=["Venta", "Alquiler"], default="Venta")

    console.print(f"\n[yellow]--- Resumen ---[/yellow]")
    console.print(f"Propiedad: {nombre} | Precio: {precio}")

    if Confirm.ask("\n¿Guardar propiedad?"):
        # Guardar en lista
        nueva_propiedad = {
            "nombre": nombre,
            "direccion": direccion,
            "precio": precio,
            "tipo": tipo
        }
        propiedadesDb.append(nueva_propiedad)
        console.print(f"\n[bold green] Propiedad guardada en memoria.[/bold green]")

        asunto = f"Nueva Propiedad Registrada: {nombre}"
        mensaje = f"Se registro la propiedad en {direccion} con precio {precio}"
        
        emailService.send_email("admin@test.com", asunto, mensaje)
    else:
        console.print("[red]Operación cancelada.[/red]")
    console.input("\nPresione Enter para volver...")


def getMenuAdmin():
    while True:
        console.clear()
        console.print(Panel("MENÚ ADMINISTRADOR", style="bold green", box=box.DOUBLE))
        
        table = Table(header_style="bold magenta", box=box.ROUNDED)
        table.add_column("Opción", style="cyan", justify="center")
        table.add_column("Descripción", style="white")
        
        table.add_row("1", "Gestión de Usuarios")
        table.add_row("2", "Gestión Inmobiliaria")
        table.add_row("3", "Reportes")
        table.add_row("0", "Cerrar Sesión")
        console.print(table)
        
        opcion = Prompt.ask("Seleccione opción", choices=["0", "1", "2", "3"])
        if opcion == "0":
            break
        elif opcion == "2":
            registrar_propiedad()
        else:
            console.print("[yellow]No hay aun...[/yellow]")
            console.input("Enter...")

def getMenuSale():
    while True:
        console.clear()
        console.print(Panel("MENÚ VENTAS", style="bold blue"))
        console.print("[1] Ver Propiedades\n[0] Salir")
        if Prompt.ask("Opcion") == "0": break

def getMenu():
    titulo = pyfiglet.figlet_format("SISTEMA DATUX", font="slant")
    console.print(titulo, style="bold cyan")
    
    while True:
        console.clear()
        console.print("[bold cyan]════════ LOGIN ════════[/bold cyan]")
        console.print("1. Iniciar Sesión")
        console.print("2. Salir")
        
        opcion = Prompt.ask("Opción", choices=["1", "2"])
        
        if opcion == "1":
            user_email = Prompt.ask("Usuario")
            password = Prompt.ask("Contraseña", password=True)
            usuario_encontrado = login_mock(user_email, password)
            
            if usuario_encontrado:
                console.print(f"\n[bold green]¡Bienvenido {usuario_encontrado['name']}![/bold green]")
                time.sleep(1)
                
                if usuario_encontrado['type_user'] == "admin":
                    getMenuAdmin()
                else:
                    getMenuSale()
            else:
                console.print("\n[bold red]Credenciales incorrectas (Prueba: admin@test.com / 123)[/bold red]")
                console.input("Enter para seguir...")
                
        elif opcion == "2":
            console.print("[green]Adiós![/green]")
            break

if __name__ == "__main__":
    try:
        getMenu()
    except KeyboardInterrupt:
        console.print("\nSalida forzada.")