from rich.console import Console
from rich.table import Table

console = Console()
console.print("Here is some initial data:", style="bold cyan")

table = Table(title="Minecraft Blocks")
table.add_column("Block", style="green")
table.add_column("Biome", style="cyan")
table.add_column("Rarity", style="magenta")

table.add_row("Diamond Ore", "Caves", "Rare")
table.add_row("Oak Log", "Forest", "Common")
table.add_row("Sand", "Desert", "Common")

console.print(table)
console.print("\n[bold cyan]Now enter your own Minecraft block:[/bold cyan]")

block = input("Enter the block name: ")
biome = input("Enter the biome where it is found: ")
rarity = input("Enter the rarity: ")

console.print("\n[bold green]You entered:[/bold green]")
console.print(f"Block: {block}")
console.print(f"Biome: {biome}")
console.print(f"Rarity: {rarity}")

