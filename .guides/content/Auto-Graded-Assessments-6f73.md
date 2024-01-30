----------

## Auto-Graded Assessments
Here are some quick examples of the different types of auto-graded assessments available through Codio. For a more detailed set of examples, take a look at the `Demo Guides and Assessments` project. To add an assessment, from the library or one you created yourself, click the **Assessments** button at the top of the page.

![You can select an assessment by clicking on the Assessment icon in the top right corner. There are options for auto-graded assessments, manually graded and selecting assessments from the library](https://global.codio.com/content/assessments.png)

### Learning Insights
Auto-graded assessments are linked to Codio's [Learning Insights](https://docs.codio.com/instructors/teaching/insights.html#id1) dashboard. The dashboard gives you and your students valuable feedback on performance.

### Assessment Library
Codio has an assessment library with hundreds of assessments (mostly Python and Java). You can search the assessments by entering a tag and its value. The tags are those topics in the gray boxes, and the value is what comes after. So if you wanted to see all of the Python assessments, you would use `Programming Language` as the tag and `Python` as the value. You can add additional parameters to make your search result more precise.

To explore Codio's assessment library, click the **Assessments** icon and select *Assessment* under the *Add from Library...* header.

![A list of assessments available in the Codio assessments library](.guides/img/assessment-library.png)

## Multiple Choice
The default multiple choice question only has two answers. You can add as many as you would like, and you can have multiple correct answers.

![The interface of a multiple choice question with text explaining all the features](.guides/img/multiple_choice_ui.png)


{Check It!|assessment}(multiple-choice-1981899322)

## Fill in the Blank
You can write whatever you like (sentences, code examples, etc.) for fill in the blank questions. Surround the "blanks" with `<<<` and `>>>`. You can tell Codio to show the students the possible answers. Each blank will have a drop down menu with all of the choices. You can also use [regular expressions](https://docs.codio.com/instructors/authoring/assessments/fill-in-blanks.html#fill-in-blanks) to parse student answers for a more granular evaluation.

![The interface of a fill in the blank question with text explaining all the features](.guides/img/fill_in_the_blank_ui.png)

{Check It!|assessment}(fill-in-the-blanks-2837664483)

## Parson's Problem
For a basic Parson's problem, type the correct code (in the correct order) in the text field above. If you stop here, the lines of code will be scrambled, and the student has to rearrange them. You can add incorrect code blocks (called distractors). Add these lines of code in the text field below. If you are using distractors, be sure to check the box that allows students to drag the correct code blocks into a new box. By default, indentation will be graded. If you do not want students to be penalized for indentation, be sure to check the box to disable indentation.

![The interface for setting up a Parson's problem assessment](.guides/img/new_parsons_ui.png)

{Check It!|assessment}(parsons-puzzle-1115584935)

