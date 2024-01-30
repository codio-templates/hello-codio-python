----------

## Building the Demo

Instruction through Codio is built around the guides feature. This is a brief description on how the demo on the previous page was built. Please see the [documentation](https://docs.codio.com/authoring.html#id1) for more information about content authoring with guides.

||| info
### To try this out
You’ll need to be in Edit Mode. From the top tool bar menu, select  **Tools->Guide->Edit**.


![From the Tools menu, select Guide and then Edit](.guides/img/editGuide.png)
|||

### Page Layout
Each page in the guide can have its own layout. You can select how many panels you want and what information goes in each panel. The most common layout is two panels without the tree; the guide is in one panel and the code editor is in the other. Click the **Layout** button in the top-right corner of the Codio window. You can select the layout from here. The default layout is a copy of the previous page, and Codio does not close any open tabs.

![Select 2 panels under the label "Layout"](.guides/img/layout.png)

It is a good idea to explicitly state the layout you want. Closing tabs from previous pages also keeps the UI free from unnecessary clutter.

### Code Editor
To use the code editor, add a programming file to your project. Right-click on the name of your project or book in the directory tree on the left. Select `New File...` and then type its name and file extension.

![In the New file dialog, type the name of the file you want to create under the label File Name.](.guides/img/create_new_file.png)

The next step is to load this file into a panel of your layout. Click on the Guide Editor tab, click the **Layout** button again, and click on the `Open Tabs` button. You can click the button and type the file's path to add a new file to the layout, or you can drag the file from the directory tree onto the page. 

![The contents of the panels in the layout are displayed under the Open Tabs label](.guides/img/coding_file.png)

This file will open with the guide. The file will remain opened until the student closes the tab. This is why it is a good idea to tell Codio to close any previously opened tabs when selecting the layout.

### Markdown
Guides are authored with [markdown](https://docs.codio.com/instructors/authoring/guides/markdown_content.html#id1), but you can use any HTML to author content. The drop-down text is an example of the `<details>` and `<summary>` tags.

### Images
You will notice a folder called `.guides` in the directory tree. To view the File Tree, select **View->File Tree**. All of the information in this folder is hidden from students. There is a subfolder called `img` where you can upload any images you want to appear in the guide. Right-click on the `img` folder and select `Upload...`.

![Selecting upload after ctrl-clicking or Right-clicking on the img folder.](.guides/img/upload.png)

Add the image to the guide using markdown syntax.

### Try It Button

Codio has syntax to add a [custom button](https://docs.codio.com/instructors/authoring/guides/custom_button.html#custom-buttons) to your guide. On the previous page, the `TRY IT` button runs the command `python3 python_demo.py` and prints the output to the guide. The terminal can always be added to a panel if you would rather have students interact with the command line.

### Code Visualizer
Codio integrates [Python Tutor](http://pythontutor.com/) into its platform. It works with a variety of languages (despite its name). To add a code visualizer to your guide, use the following syntax `[Code Visualizer](open_tutor your_file.py)`.

### Code Highlighting
You can create links that [highlight](https://docs.codio.com/instructors/authoring/guides/settings/opentabs.html#highlighting-lines-in-your-code) sections of code. It is important to note that opening a file with highlighting will retain the highlighting. Adding another link to open the same file without highlighting will "remove" the highlighting.