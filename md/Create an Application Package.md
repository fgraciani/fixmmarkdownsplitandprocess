## Create an Application Package

For this example, we will create a very simple Application that focuses
on arrival and departure alerts. It will include Application header
fields for message sender, recipient(s), timestamp, and alert type along
with two templates, one for arrival alerts and one for departure alerts.

1.  Right click on the Applications container and choose “Add a
    Package…”.

<img src=".//media/image56.png" style="width:3.09861in;height:5.13542in" />

1.  In the New Package dialogue box, change the *Name* field to
    something appropriate for your Application (in this example,
    “ExampleMessage”).

2.  Select the *Create Diagram* radio button.

3.  Then click OK.

<img src=".//media/image57.png" style="width:3.71927in;height:2.96916in" />

1.  This will bring up a New Diagram dialogue box. In the *Type*
    section:

    1.  Choose “UML Structural” under *Select From*.

    2.  Choose “Class” under *Diagram Types*.

> Click OK to create the Application package and its associated
> diagram[19].
>
> <img src=".//media/image58.png" style="width:6.5in;height:4.83264in" />

### Apply Schema Stereotype

In order to generate XSD schemas in Sparx EA, each package that
corresponds to a schema file needs an XSDschema stereotype applied to
it. To add an XSDschema stereotype to your package:

1.  Double click (or right click and choose “Properties…”) on your
    Application package (here called “ExampleMessage”) in Project
    Browser to open the Package dialogue box.

2.  In the newly opened Package dialogue box, click on the “…” box next
    to *Stereotype* (near the top right corner) to open the Stereotype
    dialogue box.

3.  In the newly opened Stereotype dialogue box, select “XSDschema” and
    then click OK.

4.  Then click OK in the Package dialogue box to apply the stereotype.

<img src=".//media/image59.png" style="width:6.5in;height:3.97778in" />

### Set Up Schema Properties

Once the stereotype is applied, you can configure your schema
properties, setting up a number of XSD details such as schema file name,
schema namespace, namespace prefixes, etc.

1.  Once again, double click (or right click and choose “Properties…”)
    on your Application package in Project Browser. With the XSDschema
    stereotype applied, this should now open an XSD schema Properties
    dialogue box.

<img src=".//media/image60.png" style="width:5.20906in;height:3.39631in" />

1.  Fill in values for your schema properties as appropriate for your
    Application. In this example, we will use the following values:

<!-- -->

1.  *Target Namespace* set to:
    “http://www.fixm.aero/app/example/1.0”[20].

2.  *Prefix* set to: “xmg”[21].

<!-- -->

1.  You must also fill in the *Schema File* field with the path to your
    application directory and an appropriate file name. In this example,
    the following *Schema File* entry will be used:
    .\\schemas\\applications\\examplemessage\\ExampleMessage.xsd.

> <u>IMPORTANT NOTE</u>: Sparx EA will not automatically create any of
> the directories for the path to the file specified in the *Schema
> File* field. **They must be created outside of Sparx EA before
> generating the schemas.** FIXM is natively set up to generate its
> schema files under a directory named “schemas” that is located in the
> same directory as the Sparx EA file. To save time, rather than
> creating all of the directories needed by hand, you can instead:

1.  Copy the “schemas” directory you modified back in [Initial Download
    and Setup](#initial-download-and-setup) into the directory where
    your Sparx EA file is located (in this example, the “uml”
    directory).

2.  Under the “applications” directory beneath the “schemas” directory,
    add another directory with a name appropriate for your Application
    (here “examplemessage” was used).

> In this example, this new “schemas” directory should be added to the
> “uml” directory and structured as shown below.

<img src=".//media/image61.png" style="width:2.18781in;height:3.02126in" />

1.  With all of these fields filled out, your XSD schema Properties
    dialogue box should look something like below. Click OK to save
    these settings.

<img src=".//media/image62.png" style="width:5.19864in;height:3.39631in" />

### Add Schema Description and Tags

The final step in setting up your schema details is to add a description
for your package and adjust the schema configuration settings that are
controlled in Sparx EA via tagged values.

1.  Once more, double click (or right click and choose “Properties…”) on
    your Application package in Project Browser and then click the UML
    button (near the top right corner). This will bring you back to your
    Package dialogue box.

2.  In the central text box, fill in a description of your Application
    package. The text entered here will also show up as a documentation
    element in your schema file.

3.  Next, click on the *Tags* tab (near the lower right hand corner) to
    add three tags used by Sparx EA when creating your schema files:
    attributeFormDefault, elementFormDefault, and version.

    1.  FIXM standardly sets attributeFormDefault to “unqualified”.

    2.  FIXM standardly sets elementFormDefault to “qualified”.

    3.  Version should be set as appropriate for your Application
        (“1.0.0” in this example).

> To add these tags, click on the third icon from the left
> \[<img src=".//media/image63.png" style="width:0.19001in;height:0.15347in" />\]
> in the *Tags* tab and fill in the *Tag* and *Value* fields similar to
> what is shown below.
>
> <img src=".//media/image64.png" style="width:3.76094in;height:1.81275in" />
>
> <img src=".//media/image65.png" style="width:3.76094in;height:1.81275in" />
>
> <img src=".//media/image66.png" style="width:3.76094in;height:1.80233in" />

1.  When finished, your Package dialogue box will look something like
    below. Click OK to save these settings.

<img src=".//media/image67.png" style="width:6.5in;height:3.98056in" />

