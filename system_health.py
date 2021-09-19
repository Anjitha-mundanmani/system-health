import os
from rich.console import Console
from rich.text import Text
console = Console()

def rich_func(res):
	console.print(Text(res,style="bold blue"))

def Dis_avail_ram():
	ram = os.popen("cat /proc/meminfo").read()
	rich_func(ram)
	

def Dis_load_avearge():
	res = os.popen("cat /proc/loadavg").read()
	rich_func(res)
	

def Dis_hostname_details():
	res = os.popen("hostnamectl status").read()
	rich_func(res)
	

def Dis_all_process_count():
	res = os.popen("ps -a | wc -l").read()
	rich_func(res)
	

def Dis_time():
	res = os.popen("uptime -s").read()
	rich_func(res)
	


def main_menu():
	console.print("1.Display available Ram",style="bold cyan")
	console.print("2.Display load avearge",style="bold cyan")
	console.print("3.Display hostname details",style="bold cyan")
	console.print("4.Display all process count",style="bold cyan")
	console.print("5.Display uptime",style="bold cyan")
	console.print("6.Exit",style="bold cyan")

operations = {
    "1":Dis_avail_ram,
    "2":Dis_load_avearge,
    "3":Dis_hostname_details,
    "4":Dis_all_process_count,
    "5":Dis_time
}

while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
