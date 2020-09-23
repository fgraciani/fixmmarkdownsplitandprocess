## Create Extension Content

The steps so far have centered on creating and setting up the
Extension’s root package. The number and organization of additional
Extension packages created below the root package (called
“subcomponents” in this document to more easily distinguish them from
the root package) will depend entirely on what the Extension is trying
to accomplish. In this very simple example, the Extension will be used
to:

-   Add a new field called “position” to the EnRoute section of Core to
    report a flight’s current whereabouts.

-   Add a new field called “sequenceNumber” to the BasicMessage section
    to help with message ordering.

The steps below describe how to create the subcomponents that will be
used to contain these new fields.

### Create an Extension Subcomponent

This example will start with creating a subcomponent for the “position”
field. Many of the steps outlined here are very similar to the steps
listed in the [Create an Extension Root Package](#_Create_an_Extension)
section above. The main difference is that Extension subcomponents
contain diagrams and Extension classes.

1.  Right click on the your Extension package and choose “Add a
    Package…”.

2.  Change the *Name* field in the New Package dialogue box to something
    appropriate to your subcomponent (in this example,
    “ExampleEnRoute”).

3.  Select the *Create Diagram* radio button.

4.  Then click OK.

> <img src=".//media/image208.png" style="width:3.75052in;height:2.99in" />

1.  This will bring up a New Diagram dialogue box. In the *Type*
    section:

    1.  Choose “UML Structural” under *Select From*.

    2.  Choose “Class” under *Diagram Types*.

> Click OK to create the subcomponent and its associated diagram.
>
> <img src=".//media/image209.png" style="width:5.9375in;height:4.40301in" />

1.  Next, apply the XSDschema stereotype to your subcomponent as
    described in the [Apply Schema
    Stereotype](#_Applying_Schema_Stereotype) section above.

2.  After the stereotype is applied, continue the schema setup as
    described in [Set Up Schema Properties](#set-up-schema-properties)
    above. The following property values should be used for this
    subcomponent in this example:

<!-- -->

1.  *Target Namespace* set to: “http://www.fixm.aero/ext/example/1.0”.

2.  *Prefix* set to: “xmp”.

3.  *Schema File* set to:
    “.\\schemas\\extensions\\example\\ExampleEnRoute.xsd”.

> <u>NOTE</u>: For this and other subcomponents, you should be able to
> skip the step of setting up additional namespaces for imported
> packages. Sparx EA should automatically generate these as needed.
>
> When finished, your XSD schema Properties dialogue box should look
> something like below.
>
> <img src=".//media/image210.png" style="width:5.20906in;height:3.39631in" />

1.  Click OK to save these settings.

2.  Reopen the subcomponent and finish the schema setup as described in
    [Add Schema Description and Tags](#add-schema-description-and-tags).
    As described in that section, the following tags should be added:

<!-- -->

1.  An attributeFormDefault tag set to: “unqualified”.

2.  An elementFormDefault tag to: “qualified”.

3.  A version tag set to an appropriate version for your Extension
    (“1.0.0” for this example).

### Create an Extension Class

Now it is time to create any Extension classes needed. This is typically
done in FIXM by creating new classes that generalize the extension
classes (the classes used throughout Core by its extension hooks) found
in the Extension package located under Core’s Base package (not to be
confused with the similarly referred to “Extension package” you are in
the process of creating).

1.  Double click on your subcomponent’s diagram (or right click it and
    choose “Open”) to get started.

2.  Next, in Toolbox, click on “Complex Type” and then click anywhere in
    the diagram section of the screen. This will open up an XSD
    complexType Properties dialogue box.

3.  Add an appropriate *Name* and *Annotation* for your new class.

4.  Then click OK.

> <img src=".//media/image68.png" style="width:1.43431in;height:3.464in" />
> <img src=".//media/image211.png" style="width:4.616in;height:3.48307in" />

1.  Next, right click on your newly created class and choose “Advanced”
    and then “Parent…” to bring up the Set Parents and Interfaces
    dialogue box.

> <img src=".//media/image212.png" style="width:3.792in;height:4.19794in" />

1.  In the *Add New Relation* section of the dialogue box, set *Type* to
    “Generalizes” and then click on “Choose…” to open up the Select
    Classifier dialogue box.

2.  From there, navigate to Fixm -&gt; Core -&gt; Base -&gt; Extension
    and then choose the Extension class you wish to target. In this
    example, it will be “EnRouteExtension”.

3.  Then click OK.

> <img src=".//media/image213.png" style="width:6.5in;height:2.59444in" />

1.  Once this is done, you should see that EnRouteExtension is now
    listed in the *Type Details* section of the Set Parents and
    Interfaces dialogue box and is also shown in italics at the top of
    your class in the diagram. Your new class now extends the
    EnRouteExtension extension hook from Core and is ready to be used to
    hold your Extension fields. Click Close.

> <img src=".//media/image214.png" style="width:6.5in;height:3.40833in" />

### Add Extension Class Content

You can now begin to add content to your new Extension class.

1.  Right click on the class in the diagram and choose “Features and
    Properties” and then “Attributes…”. This opens the Features dialogue
    box. In the Features dialogue box, you can add any attributes[35]
    needed for your Extension to your class.

> <img src=".//media/image215.png" style="width:4.61571in;height:4.272in" />

1.  Begin by clicking where it says “New Attribute…” under *Name* and
    filling in your new field’s name. In this example, that will be
    “position”.

2.  Then hit the tab key or otherwise click out of the *Name* field.

3.  You should now have a new attribute added to your class with a
    default *Type* of “int” and *Scope* of “Private”.

> <img src=".//media/image216.png" style="width:6.5in;height:3.41181in" />

1.  Next, click on the *Type* field, select the down arrow on the right
    side, and then click “Select Type…”.

> <img src=".//media/image217.png" style="width:2.43784in;height:2.1253in" />

1.  This opens the Select Type dialogue box. Navigate to the appropriate
    class in the Base package you want to use, select it, and then click
    OK. In this example, that will be Fixm -&gt; Core -&gt; Base -&gt;
    AeronauticalReference -&gt; GeographicalPosition.

> <img src=".//media/image218.png" style="width:6.48007in;height:4.89652in" />

1.  Next change the *Scope* field to “Public”.

2.  Adjust the *Multiplicity* in the *Attribute* section as needed (in
    this example, it should be set to 0..1).

3.  Then add a description for the field in the *Notes* section. When
    finished, your Features dialogue box will look something like below.

> <img src=".//media/image219.png" style="width:6.5in;height:3.89444in" />

1.  Most optional fields in FIXM are also nillable. If you wish to make
    your field nillable:

<!-- -->

1.  Click on the *Tagged Values* tab.

2.  Click on *Attribute*.

3.  Click on the third icon from the left
    \[<img src=".//media/image63.png" style="width:0.19001in;height:0.15347in" />\]
    at the top of the tab to add a new tag.

4.  In the *Tag* field type “nillable” and in *Value* type “true” and
    then click OK.

> <img src=".//media/image220.png" style="width:3.7401in;height:1.77108in" />

1.  Continue adding as many attributes as desired. When finished, click
    Close on the Features dialogue box. The class diagram should display
    the name, type, and multiplicity of each attribute added to the
    class.

> <img src=".//media/image221.png" style="width:2.17739in;height:0.84387in" />

1.  When satisfied with the subcomponent, right click on its name at the
    top of the diagram and click “Save Changes to ‘\[diagram name\]’”.

> <img src=".//media/image222.png" style="width:4.15683in;height:2.22948in" />

The class content presented here is simple but keep in mind that as many
attributes and additional Extension-defined classes can be added to this
extension hook as needed.

Along the same lines, the steps detailed under [Create Extension
Content](#_Create_Extension_Content) can be used to add as many
additional subcomponents as needed to hold additional extension hooks or
Extension-specific packages.

Below are a series of screenshots capturing key steps along the way to
creating a second subcomponent for representing the “sequenceNumber”
field needed for extending BasicMessage. The only notable difference
between creating this subcomponent and the previous one is that the
ExampleMessage class created generalizes an extension hook class from
BasicMessage under Applications rather than a class from Extensions
under Base.

<img src=".//media/image223.png" style="width:2.65582in;height:2.12019in" /><img src=".//media/image224.png" style="width:3.27079in;height:2.11947in" />

<img src=".//media/image225.png" style="width:2.959in;height:2.21775in" />
<img src=".//media/image226.png" style="width:3.39987in;height:2.20247in" />

<img src=".//media/image227.png" style="width:6.5in;height:3.25278in" />

