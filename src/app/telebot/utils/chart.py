import matplotlib.pyplot as plt


def create_budget_chart(budgets, save_path):
    data = [sum(budget.income for budget in budgets),
            sum(budget.consumption for budget in budgets),
            sum(budget.profit for budget in budgets)]
    labels = ['Income', 'Consumption', 'Profit']

    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=labels, autopct='%1.1f%%', colors=['#007acc', '#ff6384', '#4bc0c0'])
    plt.title('Budget Pie Chart')

    plt.savefig(save_path)
    plt.close()

    return save_path
