fin = open("whole.md", "rt")
fout = open("md/intro.md", "wt")
fsidebar = open("sidebar.md", "wt")

for line in fin:
  if line.startswith('# '):
    new_section = line.replace('# ', '')
    new_section = new_section.replace('\n', '')
    fsidebar.write('\n')
    fsidebar.write('\n')
    fsidebar.write('- **'+new_section+'**')
    fsidebar.write('\n')
  elif line.startswith('## '):
    print(line)
    fout.close()
    new_chapter = line.replace('## ', '')
    new_chapter = new_chapter.replace('/', '')
    new_chapter = new_chapter.replace('\n', '')
    fout = open('md/'+new_chapter+".md", "wt")
    fout.write(line)
    fsidebar.write('  - ['+new_chapter+']('+new_chapter+'.md)')
    fsidebar.write('\n')
  else:
    fout.write(line)

fin.close()
fout.close()
fsidebar.close()