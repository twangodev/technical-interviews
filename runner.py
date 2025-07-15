#!/usr/bin/env python3
"""
Interactive Solutions Runner for Technical Interview Problems
"""

import importlib.util
import inspect
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional

from fuzzywuzzy import fuzz
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table

console = Console()

class SolutionRunner:
    def __init__(self, solutions_dir: str = "leetcode"):
        self.solutions_dir = Path(solutions_dir)
        self.problems: Dict[int, Dict[str, Any]] = {}
        self.scan_problems()
    
    def scan_problems(self):
        """Scan the solutions directory and extract problem information"""
        console.print("[blue]Scanning solutions directory...[/blue]")
        
        for file_path in self.solutions_dir.glob("*.py"):
            if file_path.name.startswith("__"):
                continue
                
            # Extract problem number and title from filename
            filename = file_path.stem
            parts = filename.split("-", 1)
            
            if len(parts) >= 2 and parts[0].isdigit():
                problem_num = int(parts[0])
                title = parts[1].replace("-", " ").title()
                
                self.problems[problem_num] = {
                    "title": title,
                    "file_path": file_path,
                    "filename": filename
                }
        
        console.print(f"[green]Found {len(self.problems)} solutions[/green]")
    
    def display_all_problems(self):
        """Display all problems in a formatted table"""
        table = Table(title="Available Problems")
        table.add_column("Problem #", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("File", style="green")
        
        for num in sorted(self.problems.keys()):
            problem = self.problems[num]
            table.add_row(
                str(num),
                problem["title"],
                problem["filename"]
            )
        
        console.print(table)
    
    def search_problems(self, query: str) -> List[Tuple[int, int]]:
        """Search problems by keyword with fuzzy matching"""
        results = []
        
        for num, problem in self.problems.items():
            # Search in title
            title_score = fuzz.partial_ratio(query.lower(), problem["title"].lower())
            
            # Search in file content
            try:
                with open(problem["file_path"], 'r') as f:
                    content = f.read()
                    content_score = fuzz.partial_ratio(query.lower(), content.lower())
            except:
                content_score = 0
            
            max_score = max(title_score, content_score)
            if max_score > 60:  # Threshold for relevance
                results.append((num, max_score))
        
        return sorted(results, key=lambda x: x[1], reverse=True)
    
    def load_solution(self, problem_num: int) -> Optional[Any]:
        """Dynamically load a solution class from file"""
        if problem_num not in self.problems:
            return None
        
        file_path = self.problems[problem_num]["file_path"]
        
        try:
            # Add List import for solutions that use it
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Check if List is used but not imported
            if "List[" in content and "from typing import" not in content:
                content = "from typing import List\n" + content
            
            # Create a temporary module
            spec = importlib.util.spec_from_file_location("solution", file_path)
            module = importlib.util.module_from_spec(spec)
            
            # Execute the modified content
            exec(content, module.__dict__)
            
            # Find the Solution class
            for name, obj in module.__dict__.items():
                if inspect.isclass(obj) and name == "Solution":
                    return obj()
            
            return None
        except Exception as e:
            console.print(f"[red]Error loading solution: {e}[/red]")
            return None
    
    def run_solution(self, problem_num: int):
        """Run a specific solution interactively"""
        if problem_num not in self.problems:
            console.print(f"[red]Problem {problem_num} not found[/red]")
            return
        
        problem = self.problems[problem_num]
        console.print(Panel(f"[bold]Problem {problem_num}: {problem['title']}[/bold]"))
        
        # Load solution
        solution = self.load_solution(problem_num)
        if not solution:
            console.print("[red]Could not load solution[/red]")
            return
        
        # Show available methods
        methods = [name for name, method in inspect.getmembers(solution, predicate=inspect.ismethod)
                  if not name.startswith('_')]
        
        if not methods:
            console.print("[red]No solution methods found[/red]")
            return
        
        if len(methods) == 1:
            method_name = methods[0]
        else:
            console.print("Available methods:")
            for i, method in enumerate(methods, 1):
                console.print(f"{i}. {method}")
            
            choice = IntPrompt.ask("Select method", choices=[str(i) for i in range(1, len(methods) + 1)])
            method_name = methods[choice - 1]
        
        method = getattr(solution, method_name)
        
        # Get method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        console.print(f"\n[blue]Method signature: {method_name}{sig}[/blue]")
        
        # Get test inputs
        console.print("\n[yellow]Enter test inputs (or 'q' to quit):[/yellow]")
        
        while True:
            try:
                args = []
                for param in params:
                    if param == 'self':
                        continue
                    
                    value = Prompt.ask(f"Enter {param}")
                    if value.lower() == 'q':
                        return
                    
                    # Try to evaluate as Python literal
                    try:
                        args.append(eval(value))
                    except:
                        args.append(value)
                
                # Run the method
                console.print(f"\n[green]Running {method_name}({', '.join(map(str, args))})[/green]")
                result = method(*args)
                console.print(f"[bold green]Result: {result}[/bold green]")
                
                if not Prompt.ask("\nRun another test?", choices=["y", "n"], default="y") == "y":
                    break
                    
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
                if not Prompt.ask("Try again?", choices=["y", "n"], default="y") == "y":
                    break
    
    def main_menu(self):
        """Main interactive menu"""
        console.print(Panel("[bold cyan]Technical Interview Solutions Runner[/bold cyan]"))
        
        while True:
            console.print("\n[bold]Choose an option:[/bold]")
            console.print("1. List all problems")
            console.print("2. Search problems")
            console.print("3. Run specific problem")
            console.print("4. Exit")
            
            choice = Prompt.ask("Enter choice", choices=["1", "2", "3", "4"])
            
            if choice == "1":
                self.display_all_problems()
            
            elif choice == "2":
                query = Prompt.ask("Enter search query")
                results = self.search_problems(query)
                
                if not results:
                    console.print("[red]No results found[/red]")
                    continue
                
                console.print(f"\n[green]Found {len(results)} results:[/green]")
                for i, (num, score) in enumerate(results[:10], 1):
                    problem = self.problems[num]
                    console.print(f"{i}. Problem {num}: {problem['title']} (Score: {score})")
                
                if Prompt.ask("Run a problem?", choices=["y", "n"], default="n") == "y":
                    try:
                        choice_num = IntPrompt.ask("Enter problem number", choices=[str(r[0]) for r in results])
                        self.run_solution(choice_num)
                    except:
                        console.print("[red]Invalid selection[/red]")
            
            elif choice == "3":
                problem_num = IntPrompt.ask("Enter problem number")
                self.run_solution(problem_num)
            
            elif choice == "4":
                console.print("[blue]Goodbye![/blue]")
                break

def main():
    runner = SolutionRunner()
    runner.main_menu()

if __name__ == "__main__":
    main()