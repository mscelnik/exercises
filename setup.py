""" Script to convert solutions to exercises.
"""

__author__ = "Matthew Celnik"
__copyright__ = "Matthew Celnik"
__email__ = "matthew@celnik.co.uk"


def build_exercises(source_folder, dest_fldr):
    """ Strip solutions out of exercises and save them to a new folder.
    """
    import os
    import os.path
    import re
    import shutil

    # Ensure the destination folder exists.
    os.makedirs(dest_fldr, exist_ok=True)

    # We need two folders in the destination folder, one for the exercises
    # without solutions, and one with the solutions.  In both files, we delete
    # the marker comments.
    base_exer_fldr = os.path.join(dest_fldr, 'exercises')
    base_soln_fldr = os.path.join(dest_fldr, 'solutions')
    os.makedirs(base_exer_fldr, exist_ok=True)
    os.makedirs(base_soln_fldr, exist_ok=True)

    # Regular expression to match solution blocks in file.
    pattern = re.compile(
        '(# <<<<<<< SOLUTION\n)(?P<soln>.*?)(# =======\n)', re.DOTALL)

    # Loop over all Python files in the solutions and convert.
    for root, dirs, files in os.walk(source_folder):
        # Get the relative folder.  We mirror the structure in both the
        # destination exercise and solution folders.
        relative_fldr = root.replace(source_folder, '')
        soln_fldr = os.path.join(base_soln_fldr, relative_fldr)
        exer_fldr = os.path.join(base_exer_fldr, relative_fldr)
        os.makedirs(exer_fldr, exist_ok=True)
        os.makedirs(soln_fldr, exist_ok=True)

        # Copy all files to the destination folders.  For Python code files, we
        # first remove the solution sections/comments.
        for f in files:
            if f.endswith('.py'):
                with open(os.path.join(root, f), 'r') as fin:
                    soln = fin.read()
                exer = soln[:]

                matches = pattern.finditer(soln)
                for match in matches:
                    exer = pattern.sub('', exer, count=1)
                    soln = pattern.sub('\g<soln>', soln, count=1)

                # Write the files to the destination folders.
                with open(os.path.join(soln_fldr, f), 'w') as fout:
                    fout.write(soln)
                with open(os.path.join(exer_fldr, f), 'w') as fout:
                    fout.write(exer)
            else:
                # Copy other files as they are to both destinations.
                shutil.copyfile(os.path.join(root, f),
                                os.path.join(soln_fldr, f))
                shutil.copyfile(os.path.join(root, f),
                                os.path.join(exer_fldr, f))


def create_zip(dist_fldr, zip_path):
    """ Create a zip file containing the distribution files.

    Args:
        dist_fldr = Path to folder containing the distribution.
        zip_path = Path to the ZIP file containing the distribution.

    Disk:
        Writes a zip file to the distribution folder, containing everything in
        the distribution folder.
    """
    import os
    import os.path
    import zipfile

    # Ensure the destination folder exists.
    os.makedirs(os.path.dirname(zip_path), exist_ok=True)

    with zipfile.ZipFile(zip_path, mode='w') as zout:
        for root, dirs, files in os.walk(dist_fldr):
            relative_fldr = root.replace(dist_fldr, '')
            for f in files:
                zout.write(os.path.join(root, f),
                           os.path.join(relative_fldr, f))


if __name__ == '__main__':
    build_fldr = 'build'
    build_exercises('exercises', build_fldr)
    create_zip(build_fldr, 'dist/distro.zip')
