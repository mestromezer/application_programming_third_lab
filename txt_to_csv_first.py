import csv
import os


def write_as_csv(paths_to_files: str) -> None:
    
    """Writes path to files from dataset in CSV file
    """

    with open("dataset_csv_first.csv", "w+", encoding='utf-8', newline='') as file:
        csv_file = csv.writer(file, delimiter=';')
        csv_file.writerow(["Absolute path", "Relative path", "Class"])

        for i in range(0, len(paths_to_files)):
            #print(f'../{paths_to_files[i][22::]}')
            csv_file.writerow([f'{paths_to_files[i]}',
                              f'../{paths_to_files[i][22::]}', f'{paths_to_files[i][-10]}'])


def get_paths_to_files(path_to_dataset: str) -> str:
    """Gets path to files from dataset given

    Args:
        path_to_dataset (str): path to source folder (dataset)

    Returns:
        str: list of paths to files
    """
    paths_to_files = list()

    for folder_num in range(1, 6):
        
        folder_path = path_to_dataset+'/'+str(folder_num)
        num_of_files = sum(os.path.isfile(os.path.join(folder_path, f))
                           for f in os.listdir(folder_path)) + 1

        for file_num in range(1, num_of_files):
            path_to_file = path_to_dataset + folder_path+f'/{(file_num):04}'+'.txt'
            paths_to_files.append(path_to_file[len(path_to_dataset):])

    return paths_to_files


if __name__ == '__main__':

    path_to_dataset = os.path.abspath("../application_programming_first_lab_and_dataset/dataset")
    paths_to_files = get_paths_to_files(path_to_dataset)

    write_as_csv(paths_to_files)

    print("Работа окончена")
