def read_source_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def compile_logic(source_code):
    # This is where your Lexer, Parser, and Code Generator will go.
    # For now, we are just doing a silly placeholder transformation.
    lines = source_code.splitlines()
    custom_instructions = []
    
    for line in lines:
        if line.strip():
            custom_instructions.append(f"EXECUTE_LINE: {line.strip()}")
            
    return "\n".join(custom_instructions)

def write_compiled_file(file_path, compiled_data):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(compiled_data)

# Main execution
def main():
    source = "input_script.py"
    destination = "output_script.custom"
    
    # 1. Read
    raw_code = read_source_file(source)
    
    # 2. Compile
    compiled_code = compile_logic(raw_code)
    
    # 3. Write
    write_compiled_file(destination, compiled_code)
    print("Compilation complete!")

if __name__ == "__main__":
    main()