# drone-imagery-notes
A colleection of learnings while exploring processing and storage of drone imagery during my masters research project


## Agisoft Metashape

### Standard edition vs Professional Edition
The killer feature in professional edition is the ability to 

### Project Size
Realistically you probably can't fit all of your source data into a single project and have it build successfully without crashing. I found the sweetspot to be around 1000 images on a modern desktop (i5-14600K, RTX4060Ti 16GB, 32GB RAM).

### Storage
Agisoft Metashape projects will eat your harddrive for breakfast, come prepared with LOTS of free storage space. This is because they effectively make multiple copies of every imported image inside the metashape project file as it builds the orthomosaic. See below for how ~9GB of JPG images produces a 25GB+ metashape project file.

 ![Figure: Metashape Project File Loves Storage Space](./images/metashape_project_file_size.png)




### Student Licenses
Agisoft offers cheaper pricing for education licences if you want to run this software on your own PC (as of writing US$59 for the standard edition, which is what I used):

https://www.agisoft.com/buy/online-store/educational-license/
