import os
import numpy as np
def split_file(file_path, output_dir, num_files, lines_per_file, floats_per_line):
    with open(file_path, "r") as f:
        matrix = np.genfromtxt(f, dtype=np.float32)
        file_index = 0
        for chunk_index in range(num_files):
            output_file_path = os.path.join(output_dir, f"m{file_index}.txt")
            with open(output_file_path, "w") as outf:
                chunk_start = chunk_index * lines_per_file * floats_per_line
                chunk_end = min((chunk_index + 1) * lines_per_file * floats_per_line, len(matrix))
                chunk = matrix[chunk_start:chunk_end]
                for element in chunk.reshape(lines_per_file, floats_per_line):
                    for item in element:
                        outf.write(f"{item} ")
                    outf.write("\n")
                file_index += 1
if __name__ == '__main__':
    file_path, output_dir = "colin.txt", "de"
    num_files, lines_per, floats_per = 8, 28, 12
    split_file(file_path, output_dir, num_files, lines_per, floats_per)

