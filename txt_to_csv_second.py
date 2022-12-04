import csv
import os
import shutil


def write_as_csv(path_to_dataset: str, paths_to_files: str):
    """Writes as CSV 

    Args:
        path_to_dataset (_type_): path to source
        paths_to_files (_type_): content from source
    """
    with open("dataset_csv_first.csv", "w+", encoding='utf-8', newline='') as file:
        csv_file = csv.writer(file, delimiter=';')
        csv_file.writerow(["Absolute path", "Relative path", "Class"])

        for path in paths_to_files:
            path = path[0:2] + '_' + path[3:] #raplce / with _
            csv_file.writerow([f'{path_to_dataset+path}',
                              f'../application_programming_first_lab_and_dataset/dataset{path}', f'{path[1]}'])


def mk_newdataset(nd_path: str):
    """creates new dataset

    Args:
        nd_path (_type_): new dataset's path
    """
    os.mkdir(nd_path)


def copy_dataset(path_to_dataset: str) -> str:
    """Copies dataset to the new direct

    Args:
        path_to_dataset (str): Path to old one

    Returns:
        str: Path to the new one
    """
    nd_path='./new_dataset'
    mk_newdataset(nd_path)

    for folder_num in range(1,6):

        folder_path = path_to_dataset+'/'+str(folder_num) #path to current folder (mark 1-5)

        num_of_files = sum(os.path.isfile(os.path.join(folder_path, f)) #amount of files in current folder
                           for f in os.listdir(folder_path)) + 1

        for file_num in range(0, (num_of_files - 1)):
            shutil.copy(folder_path+f"/{(file_num+1):04}.txt", nd_path) #rewrite
            os.rename(f"./new_dataset/{(file_num+1):04}.txt", f"./new_dataset/{folder_num}_{(file_num+1):04}.txt") #rename
    
    return nd_path


def get_paths_to_files(path_to_dataset: str) -> str:
    """Gets paths to files from dataset

    Args:
        path_to_dataset (str): Path to get files from

    Returns:
        str: List of paths
    """
    paths_to_files = list()

    for folder_num in range(1, 6):
        folder_path = path_to_dataset+'/'+str(folder_num)
        num_of_files = sum(os.path.isfile(os.path.join(folder_path, f))
                           for f in os.listdir(folder_path)) + 1

        for file_num in range(1, num_of_files):
            path_to_file = folder_path+f'/{(file_num):04}'+'.txt'
            print(f'{folder_num} : {(file_num):04}')
            paths_to_files.append(path_to_file[len(path_to_dataset):])

    return paths_to_files


if __name__ == '__main__':

    path_to_dataset = os.path.abspath("../application_programming_first_lab_and_dataset/dataset")
    paths_to_files = get_paths_to_files(path_to_dataset)

    new_dataset_path = copy_dataset(path_to_dataset)

    write_as_csv(new_dataset_path, paths_to_files)

    print("Работа окончена")
