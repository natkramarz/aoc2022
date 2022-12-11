import re


class Directory:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self._size = None 
        self.children = {}
    
    @property
    def size(self):
        if self._size:
            return self._size
        dir_size = 0
        for child in self.children.values():
            dir_size += child.size
        return dir_size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def get_smaller_directories_total_size(curr):
    curr_sum = 0
    if isinstance(curr, Directory):
        for child in curr.children.values():
            curr_sum += get_smaller_directories_total_size(child)
        if curr.size <= 100_000:
            return curr_sum  + curr.size
    return curr_sum

def find_minimimum_space_size_to_delete(curr, curr_min, space_to_free_up):
    if isinstance(curr, File):
        return curr_min
    if isinstance(curr, Directory): 
        for child in curr.children.values():
            if child.size >= space_to_free_up:
                curr_min = min(find_minimimum_space_size_to_delete(child, curr_min, space_to_free_up), curr_min)
    if curr.size >= space_to_free_up:
        return  min(curr.size, curr_min)
    return curr_min 

with open("tests/day7.txt") as f:
    root = None
    curr_dir = None
    for line in f:
        processed_line = line.rstrip()
        matched = re.match("^\$ cd (.+)?", processed_line) 
        if matched:
            if matched.groups()[0] == "/":
                root = Directory("/")
                curr_dir = root
            else:
                if matched.groups()[0] == "..":
                    if curr_dir is not root:
                        curr_dir = curr_dir.parent
                else:
                    curr_dir =  curr_dir.children[matched.groups()[0]]
        else:
            matched = re.match("^\$ ls", processed_line)
            if not matched:
                matched = re.match("^dir (.*)", processed_line)
                if matched:
                    curr_dir.children[matched.groups()[0]] = Directory(matched.groups()[0], curr_dir)
                else:
                    matched = re.match("^(.*) (.*)", processed_line)
                    if matched:
                        curr_dir.children[matched.groups()[0]] = File(matched.groups()[1], int(matched.groups()[0]))

    # part 1
    print(get_smaller_directories_total_size(root))
    
    # part 2
    TOTAL_DISK_SPACE = 70_000_000
    NEEDED_SPACE = 30_000_000
    unused_disk_space = TOTAL_DISK_SPACE - root.size
    space_to_free_up = NEEDED_SPACE - unused_disk_space
    print(find_minimimum_space_size_to_delete(root, root.size, space_to_free_up))