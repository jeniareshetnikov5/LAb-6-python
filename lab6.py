with open('mailbox.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

unique_senders = set()
unique_domains = set()
unique_confidences = set()
unique_cyrus_versions = set()

shortest_line = None

for line in lines:
    stripped_line = line.strip()

    # Задача 1: Уникальные имена аккаунтов отправителей из поля "From:"
    if line.startswith('From:'):
        parts = line.split(':')
        if len(parts) > 1:
            email = parts[1].strip()
            if '@' in email:
                account = email.split('@')[0]
                unique_senders.add(account)

    # Задача 4: Уникальные доменные имена отправителей из поля "From:"
    if line.startswith('From:'):
        parts = line.split(':')
        if len(parts) > 1:
            email = parts[1].strip()
            if '@' in email:
                domain = email.split('@')[1]
                unique_domains.add(domain)

    # Задача 5: Уникальные значения X-DSPAM-Confidence:
    if line.startswith('X-DSPAM-Confidence:'):
        conf = line.split(':')[1].strip()
        unique_confidences.add(conf)

    # Задача 11: Уникальные версии Cyrus (например, Cyrus v2.3.8 -> v2.3.8)
    if 'Cyrus v' in line:
        idx = line.find('Cyrus v')
        if idx != -1:
            sub = line[idx + 6:].split()[0]
            unique_cyrus_versions.add(sub)

    # Задача 18: Самая короткая непустая строка в файле
    if stripped_line:
        if shortest_line is None or len(stripped_line) < len(shortest_line):
            shortest_line = stripped_line

# Запись результатов в файл output.txt
with open('output.txt', 'w', encoding='utf-8') as output:
    output.write("=== Задача 1: Уникальные аккаунты отправителей ===\n")
    for acc in sorted(unique_senders):
        output.write(acc + '\n')

    output.write("\n=== Задача 4: Уникальные домены отправителей ===\n")
    for dom in sorted(unique_domains):
        output.write(dom + '\n')

    output.write("\n=== Задача 5: Уникальные уровни confidence ===\n")
    for conf in sorted(unique_confidences):
        output.write(conf + '\n')

    output.write("\n=== Задача 11: Уникальные версии Cyrus ===\n")
    for ver in sorted(unique_cyrus_versions):
        output.write(ver + '\n')

    output.write("\n=== Задача 18: Самая короткая строка ===\n")
    output.write(str(shortest_line) + '\n')

print("Обработка завершена. Результаты успешно записаны в output.txt.")