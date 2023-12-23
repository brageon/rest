import os, shutil
def chunk_file(input_file, num_chunks, chunk_size):
    output_folder = os.path.splitext(input_file)[0]
    os.makedirs(output_folder, exist_ok=True)
    with open(input_file, 'r') as f:
        text = f.read()
    chunks = []
    for i in range(0, len(text), chunk_size * 16):
        chunks.append(text[i:i + chunk_size * 16])
    chunk_index = 0
    for chunk in chunks:
        output_file = os.path.join(output_folder, f"v{chunk_index:0}.txt")
        with open(output_file, 'w') as f:
            f.write(chunk)
        chunk_index += 1
if __name__ == "__main__":
    input_file = "far2.txt"
    num_chunks = 12
    chunk_size = 279
    chunk_file(input_file, num_chunks, chunk_size)
