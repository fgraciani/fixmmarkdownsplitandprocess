fin = open("docs/whole.md", "rt")
fout = open("docs/intro.md", "wt")
fsidebar = open("docs/_sidebar.md", "wt")
first_time = True

for line in fin:
  if line.startswith('# '):
    new_section = line.replace('# ', '')
    new_section = new_section.replace('\n', '')
    if first_time :
      pass
    else:
      fsidebar.write('\n')
      fsidebar.write('\n')
    first_time = False
    fsidebar.write('- **'+new_section.rstrip()+'**')
    fsidebar.write('\n')
  elif line.startswith('## '):
    print(line)
    fout.close()
    new_chapter = line.replace('## ', '')
    new_chapter = new_chapter.replace('/', '')
    new_chapter = new_chapter.replace('\n', '')
    new_chapter_file_name="".join(x for x in new_chapter if x.isalnum())
    fout = open('docs/'+new_chapter_file_name+".md", "wt")
    fout.write(line)
    fsidebar.write('  - ['+new_chapter.rstrip()+']('+new_chapter_file_name+'.md)')
    fsidebar.write('\n')
  else:
    fout.write(line)

fin.close()
fout.close()
fsidebar.close()