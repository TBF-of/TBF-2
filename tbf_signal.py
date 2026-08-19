#!/usr/bin/env python3
# ============================================
#   TBF (Series G Edition)
#   by TBFPUMBA — Live Mobile Signal Monitor
# ============================================

import os
import sys
import json
import time
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.align import Align

console = Console()

OPERATORS = {
    "25501": ("Vodafone UA", "red"),
    "25503": ("Kyivstar", "blue"),
    "25506": ("lifecell", "yellow")
}

BANNER_TBF = """[bold blue]
   ████████╗██████╗ ███████╗
   ╚══██╔══╝██╔══██╗██╔════╝
      ██║   ██████╔╝█████╗  
      ██║   ██╔══██╗██╔══╝  
      ██║   ██████╔╝██║     
      ╚═╝   ╚═════╝ ╚═╝     
[/bold blue][bright_blue]
     [ LIVE SIGNAL HUNTER ]
[/bright_blue]"""

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def get_telephony_data():
    try:
        output = subprocess.check_output(["termux-telephony-deviceinfo"], stderr=subprocess.DEVNULL)
        return json.loads(output.decode('utf-8'))
    except Exception:
        return None

def ping_host(host="8.8.8.8"):
    try:
        cmd = ["ping", "-c", "1", "-w", "1", host]
        res = subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode('utf-8')
        for line in res.split('\n'):
            if "time=" in line:
                return line.split("time=")[1].split(" ")[0] + " ms"
    except Exception:
        pass
    return "TIMEOUT / OFF"

def build_interface():
    data = get_telephony_data()

    if not data:
        return Panel(
            "[bold red]❌ Помилка Termux:API[/bold red]\n\n"
            "1. Переконайся, що встановлено додаток [bold yellow]Termux:API[/bold yellow] (з F-Droid).\n"
            "2. Встанови пакет у консолі: [bold cyan]pkg install termux-api[/bold cyan]\n"
            "3. Перевір дозволи на 'Телефон' для Termux:API у налаштуваннях Android.",
            title="TBF Signal Monitor", border_style="red"
        )

    op_code = data.get("network_operator", "")
    op_info = OPERATORS.get(op_code, (data.get("network_operator_name", "Невідомо"), "white"))
    op_name, op_color = op_info

    net_type = data.get("network_type", "N/A").upper()
    sim_state = data.get("sim_state", "N/A")
    phone_type = data.get("phone_type", "N/A").upper()
    ping_val = ping_host("8.8.8.8")

    table = Table(border_style=op_color, expand=True, show_header=True)
    table.add_column("Параметр", style="bold cyan", width=22)
    table.add_column("Значення", style="bold white")

    table.add_row("Мобільний оператор", f"[{op_color}][bold]{op_name}[/{op_color}] (Код: {op_code})")
    table.add_row("Тип мережі", f"[bold green]{net_type}[/bold green]")
    table.add_row("Тип зв'язку", phone_type)
    table.add_row("Статус SIM-карти", sim_state)
    table.add_row("Затримка (Ping 8.8.8.8)", f"[bold yellow]{ping_val}[/bold yellow]")
    table.add_row("Останнє оновлення", time.strftime("%H:%M:%S"))

    return Panel(
        table,
        title=f"[bold white] TBF Signal Monitor — [bold {op_color}]{op_name}[/bold {op_color}] [/bold white]",
        subtitle="[dim]Натисніть Ctrl+C для виходу[/dim]",
        border_style=op_color
    )

def main():
    clear()
    console.print(Align.center(BANNER_TBF))
    console.print(Align.center("[bold cyan]dev>[/bold cyan] [bold white]@TBFPUMBA[/bold white]    [bold cyan]version[/bold cyan] [bold white]1.0 (Series G)[/bold white]"))
    console.print()

    try:
        with Live(build_interface(), refresh_per_second=1, console=console) as live:
            while True:
                time.sleep(1)
                live.update(build_interface())
    except KeyboardInterrupt:
        console.print("\n[bold red][!] Моніторинг зупинено.[/bold red]")

if __name__ == "__main__":
    main()

