class Employee:
    def __init__(self, emp_id: str, name: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

  
    def category(self) -> str:
       
        if self.salary >= 70000:
            return "High Salary"
        elif 40000 <= self.salary < 70000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def __str__(self) -> str:
        return f"ID: {self.emp_id:<8} | Name: {self.name:<15} | Salary: ₹{self.salary:,.2f} | Category: {self.category}"


class Company:
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, emp_id: str, name: str, salary: float) -> None:
        """Create and add a new employee to the company."""
        employee = Employee(emp_id, name, salary)
        self.employees.append(employee)
        print(f"Added {name} (ID: {emp_id}) successfully.")

    def display_all_employees(self) -> None:
        """Display all employee records in a clean table format."""
        print(f"\n{'=' * 65}")
        print(f"               {self.company_name.upper()} - EMPLOYEE DIRECTORY")
        print(f"{'=' * 65}")
        
        if not self.employees:
            print("No employees found in the directory.")
            return

        for emp in self.employees:
            print(emp)
            
        print(f"{'=' * 65}")



if __name__ == "__main__":
  
    tech_corp = Company("TechSolutions Ltd")

   
    tech_corp.add_employee("E101", "Aarav Sharma", 85000)   
    tech_corp.add_employee("E102", "Priya Verma", 55000)    
    tech_corp.add_employee("E103", "Rohan Mehta", 32000)  
    tech_corp.add_employee("E104", "Ananya Iyer", 70000)   

   
    tech_corp.display_all_employees()
