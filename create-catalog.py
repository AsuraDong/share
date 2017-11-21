import os

if __name__=='__main__':
    root = os.path.join(".")
    for dir in os.listdir(root):
        if os.path.isdir(dir) and dir[0]!=".":
            print(
                "- [%s](./%s/README.md)" % (dir,dir)
            )
            readme_path = os.path.join(".",dir,"README.md")
            passage = "## 目录\n"
            for md in os.listdir(dir):
                md_path = os.path.join(dir,md)
                if os.path.isfile(md_path) and (os.path.splitext(md_path)[-1]==".md" or os.path.splitext(md_path)[-1]=="pdf"):
                    passage= passage +"- [%s](./%s)\n" %(os.path.splitext(md)[0],md)
            with open(readme_path,'w',encoding="utf-8") as fout:
                fout.write(passage)
            # print(" ",passage)