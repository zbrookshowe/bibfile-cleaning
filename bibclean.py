def delete_items(lines: list):
    '''
    Description: deletes language and abstract bibtex
    entries from a list of lines of a .bib file.
    '''
    # delete language
    for line in lines:
        lan_idx = line.find('language')
        if lan_idx != -1:
            lines.remove(line)

    # delete abstract
    for i, line in enumerate(lines):
        abs_idx = line.find('abstract')
        if abs_idx != -1:
            lines.remove(line)
            # deal with multi-line abstract entries
            while lines[i][-3:]!='},\n':
                lines.pop(i)
            lines.pop(i)


    return lines


def reduce_author_list(lines: list, max_num_authors: int):
    '''
    Description: trims authors down to max_num_authors in
    a list of lines from a .bib file. Does not trim if the
    author line ends with 'others'.
    '''
    # find all author entries in lines, save idxs in list
    author_line_idxs = []
    for i, line in enumerate(lines):
        author_idx = line.find('author')
        if author_idx != -1:
            author_line_idxs.append(i)
    
    # trim author line to max_num_authors authors unless it ends with 'others'
    for idx in author_line_idxs:
        author_line = lines[idx]
        author_list = author_line.split(' and ')
        if len(author_list)>max_num_authors and not author_list[-1][-9:]=='others},\n':
            author_line_trimmed = ' and '.join(author_list[:max_num_authors]) + ' and others},\n'
            lines[idx] = author_line_trimmed

    return lines




def bibclean(filename, max_num_authors):
    '''
    Description: deletes language and abstract entries from
    the .bib file specified by filename and reduces author
    list down to max_num_authors. Saves as a new file with
    the suffix '_cleaned'.
    '''
    # open file and read lines
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # delete language and abstract
    lines = delete_items(lines)

    # trim author list
    lines = reduce_author_list(lines, max_num_authors)

    # save as new file
    trimmed_filename = filename[:-4] + '_cleaned.bib'
    with open(trimmed_filename, 'w') as f:
        f.writelines(lines)

    return
    

def main():
    # open file and read lines
    filename = "missing_things.bib"
    max_num_authors = 4
    bibclean(filename, max_num_authors)
    

if __name__ == '__main__':
    main()