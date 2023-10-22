def process_text_file(input_file_path, output_file_path="rockyou_mod.dic"):
    # Leer el archivo
    with open(input_file_path, 'r', encoding='ISO-8859-1') as file:
        content = file.read()

    
    # Dividir el contenido en strings
    strings = content.split()
    
    # Contar la cantidad total de strings antes de realizar cambios
    total_strings_before = len(strings)
    
    # Filtrar los strings, eliminando aquellos que comiencen con un número y modificando los demás
    processed_strings = []
    for string in strings:
        # Si el string comienza con un número, se ignora
        if string[0].isdigit():
            continue
        # Si no, se modifica y se agrega a la lista de strings procesados
        modified_string = string.capitalize() + '0'
        processed_strings.append(modified_string)
    
    # Contar la cantidad de strings que fueron eliminados y la cantidad que quedan
    strings_deleted = total_strings_before - len(processed_strings)
    strings_remaining = len(processed_strings)
    
    # Escribir los strings procesados en el nuevo archivo
    with open(output_file_path, 'w') as file:
        file.write('\n'.join(processed_strings))
    
    return total_strings_before, strings_deleted, strings_remaining

input_file_path = '/Users/mimac/Documents/UDP/Cripto/Lab3-Cripto/rockyou.txt'
total_before, deleted, remaining = process_text_file(input_file_path)
print(f'Total de strings antes: {total_before}')
print(f'Strings eliminados: {deleted}')
print(f'Strings restantes: {remaining}')
