import os
from rich.console import Console
from rich.text import Text
console = Console()

def Display_available_RAM():
    ram = os.popen("vmstat -s").read()
    console.print(Text("Available RAM :",style="bold blue"))
    console.print(Text(ram,style="bold cyan"))

def Display_Load_avearge():
    data = os.popen("cat /proc/loadavg").read()
    console.print(Text("Load Average :",style="bold blue"))
    console.print(Text(data,style="bold cyan"))

def Display_Hostname_details():
    data = os.popen("hostnamectl status").read()
    console.print(Text("Hostname Details :",style="bold blue"))
    console.print(Text(data,style="bold cyan"))


def Display_All_process_count():
    data = os.popen("ps -aux | wc -l").read()
    console.print(Text("Process Count :",style="bold blue"))
    console.print(Text(data,style="bold cyan"))


def Display_time():
    data = os.popen("uptime -s").read()
    console.print(Text("Present Time :",style="bold blue"))
    console.print(Text(data,style="bold cyan"))


def main_menu():
	console.print("1.Display available RAM",style="bold cyan")
	console.print("2.Display Load avearge",style="bold cyan")
	console.print("3.Display Hostname details",style="bold cyan")
	console.print("4.Display All process count",style="bold cyan")
	console.print("5.Display uptime",style="bold cyan")
	console.print("6.Exit",style="bold cyan")

operations = {
    "1":Display_available_RAM,
    "2":Display_Load_avearge,
    "3":Display_Hostname_details,
    "4":Display_All_process_count,
    "5":Display_time
}

while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
