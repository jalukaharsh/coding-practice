"""Renaming files in leetcode folder to sort according to leetcode question number."""

import os


def renamer(dir_path: str) -> None: 
    """Adds 0 prefixes to all question numbers less than 100 in the leetcode folder."""
    solutions = os.listdir(dir_path)

    for solution in solutions: 

        leetcode_split = solution.split('_')
        leetcode_no = leetcode_split[0]
        new_prefix = leetcode_no
        if int(leetcode_no) < 100:
            new_prefix = '0' + leetcode_no
            if int(leetcode_no) < 10:
                new_prefix = '00' + leetcode_no

            new_file_name = new_prefix + '_' + '_'.join(leetcode_split[1:])
            new_file_path = os.path.join(dir_path, new_file_name)
            orig_file_path = os.path.join(dir_path, solution)
            os.rename(orig_file_path, new_file_path)


if __name__ == '__main__':
    renamer('leetcode')
