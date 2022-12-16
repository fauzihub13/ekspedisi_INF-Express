from rich.console import Console
from time import sleep

console = Console()

def loading():
    data = [1, 2, 3]
    with console.status("[bold green]Menghapus data...") as status:
        while data:
            num = data.pop(0)
            sleep(1)
            #console.log(f"[green]Finish fetching data[/green] {num}")

        console.log(f'[bold][red]Data Berhasil Dihapus!'); return""