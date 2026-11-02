# 1. Membuat list pesanan dan list kosong untuk pesanan yang sudah selesai
sandwich_orders = ['tuna', 'club', 'BLT', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"I made your {current_sandwich} sandwich.")
    
    finished_sandwiches.append(current_sandwich)

print("The following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"  - {sandwich.title()} sandwich")