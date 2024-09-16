import os
import sys
import shutil


def create_dataset_directories(base_dir: str) -> None:
    print("Start creation of dataset directories...")

    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    else:
        print(f"Directory {base_dir} already exists")
        return

    directories = ["train", "validation", "test"]
    for directory in directories:
        sub_dir = os.path.join(base_dir, directory)
        os.mkdir(sub_dir)
        os.mkdir(os.path.join(sub_dir, "cats"))
        os.mkdir(os.path.join(sub_dir, "dogs"))

    print("Done")


def copy_data(
    src: str, dst: str, example_name: str, start: int, end: int
) -> None:
    fnames = [[os.path.join(f"{example_name}", f"{i}.jpg"), f"{example_name}.{i}.jpg"] for i in range(start, end)]
    print("Copying...")
    for fname in fnames:
        print(f"Copying {src}/{fname[0]} to {dst}/{fname[1]}")
        shutil.copyfile(
            os.path.join(src, fname[0]),
            os.path.join(dst, fname[1])
        )


def main(argv):
    if len(argv) != 3:
        print("Bad arguments")
        sys.exit(-1)

    src, dst = argv[1], argv[2]

    create_dataset_directories(dst)

    copy_data(src, f"{dst}/train/cats/", "Cat", 1000, 2000)
    copy_data(src, f"{dst}/train/dogs/", "Dog", 1000, 2000)

    copy_data(src, f"{dst}/validation/cats/", "Cat", 2000, 2500)
    copy_data(src, f"{dst}/validation/dogs/", "Dog", 2000, 2500)

    copy_data(src, f"{dst}/test/cats/", "Cat", 2500, 3000)
    copy_data(src, f"{dst}/test/dogs/", "Dog", 2500, 3000)


if __name__ == "__main__":
    main(sys.argv)

# Run the script
# # py prepare_dataset.py downloads/kagglecatsanddogs_5340/PetImages/ dataset
# check corrupted images
# # find dataset -type f -exec file {} \; | grep -vE 'image|bitmap'
